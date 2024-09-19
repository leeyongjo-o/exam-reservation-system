from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from app.models import User
from app.serializers.userSerializer import UserSerializer
from app.utils import get_extend_schema_view_kwargs

SUBJECT = '유저'


@extend_schema(tags=[SUBJECT])
@extend_schema_view(**get_extend_schema_view_kwargs(SUBJECT, includes=['list']))
class UserViewSet(ListModelMixin, GenericViewSet):
    authentication_classes = []
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer
