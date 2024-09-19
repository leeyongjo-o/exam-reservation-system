from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.viewsets import ModelViewSet

from app.models import Reservation
from app.permissions import IsOwner
from app.serializers.reservationSerializer import ReservationSerializer
from app.utils import get_extend_schema_view_kwargs

SUBJECT = '예약'


@extend_schema(tags=[SUBJECT])
@extend_schema_view(**get_extend_schema_view_kwargs(SUBJECT))
class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_permissions(self):
        if self.request.user and self.request.user.is_admin:
            return []
        else:
            permission_classes = [IsOwner]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        if self.action == 'list':
            if self.request.user and not self.request.user.is_admin:
                return Reservation.objects.filter(user=self.request.user)
        return Reservation.objects.all()
