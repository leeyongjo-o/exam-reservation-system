from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken, AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from app.models import User


@extend_schema(tags=['로그인, 회원가입'])
class LoginView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

    def __init__(self, *args, **kwargs):
        self.serializer_class.default_error_messages = {
            'no_active_account': '아이디 또는 비밀번호를 잘못 입력했습니다.'
        }
        super().__init__(*args, **kwargs)

    @extend_schema(summary='로그인', description='사용자 로그인')
    def post(self, request, *args, **kwargs):
        try:
            User.objects.get(username=request.data.get('username'), is_active=True)
        except User.DoesNotExist:
            raise NotFound(detail='가입된 정보가 없습니다.')

        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        except AuthenticationFailed as e:
            raise e
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
