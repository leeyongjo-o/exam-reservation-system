from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.views import TokenRefreshView


@extend_schema(tags=['로그인, 회원가입'])
class LoginRefreshView(TokenRefreshView):

    @extend_schema(summary='토큰 리프레쉬')
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
