from django.urls import path, include
from rest_framework_extensions.routers import ExtendedDefaultRouter

from app.views.joinView import JoinView
from app.views.loginRefreshView import LoginRefreshView
from app.views.loginView import LoginView
from app.views.myInfoView import MyInfoView
from app.views.userViewSet import UserViewSet

user_router = ExtendedDefaultRouter(trailing_slash=False)
user_router.register(r'users', UserViewSet)

urlpatterns = [
    path('login', LoginView.as_view(), name='token_obtain_pair'),
    path('login/refresh', LoginRefreshView.as_view(), name='token_refresh'),
    path('join', JoinView.as_view(), name='join'),
    path('my/info', MyInfoView.as_view(), name='my-info'),

    # users
    path('', include(user_router.urls)),
]
