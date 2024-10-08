from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from app.models import Reservation
from app.permissions import IsOwner, IsClientUser, IsAdminUser
from app.serializers.reservationConfirmSerializer import ReservationConfirmSerializer
from app.serializers.reservationSerializer import ReservationSerializer
from app.utils import get_extend_schema_view_kwargs

SUBJECT = '예약'


@extend_schema(tags=[SUBJECT])
@extend_schema_view(**get_extend_schema_view_kwargs(SUBJECT))
class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsClientUser]  # 예약 신청은 고객만 가능
        elif self.action == 'confirm_reservation':
            permission_classes = [IsAdminUser]  # 예약 확정은 어드민만 가능
        elif self.request.user.is_authenticated and not self.request.user.is_admin:
            permission_classes = [IsOwner]  # 예약 상세 조회, 수정, 삭제 시 고객은 본인 것만 가능
        else:
            permission_classes = self.permission_classes
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        if self.action == 'list':
            if self.request.user.is_authenticated and not self.request.user.is_admin:
                return Reservation.objects.filter(user=self.request.user)    # 예약 리스트 조회 시 고객은 본인 것만 노출
        return Reservation.objects.all()

    @extend_schema(summary='예약 확정')
    @action(methods=('post',), detail=True, url_path='confirm', url_name='confirm_reservation',
            serializer_class=ReservationConfirmSerializer)
    def confirm_reservation(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'meesage': '예약 확정이 완료되었습니다.'})
