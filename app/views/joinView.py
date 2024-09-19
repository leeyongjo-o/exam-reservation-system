from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from app.serializers.userSerializer import UserSerializer


@extend_schema(
    tags=['로그인, 회원가입'],
    description='회원가입',
    request=UserSerializer,
)
class JoinView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    @extend_schema(summary='회원가입')
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '회원가입이 완료되었습니다.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
