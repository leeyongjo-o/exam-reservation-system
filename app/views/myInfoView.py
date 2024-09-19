from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.serializers.userSerializer import UserSerializer


@extend_schema(
    tags=['로그인, 회원가입'],
    responses={200: UserSerializer},
)
class MyInfoView(APIView):

    @extend_schema(summary='내 정보 조회', description='내 정보 조회')
    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
