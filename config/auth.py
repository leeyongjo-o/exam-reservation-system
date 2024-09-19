from drf_spectacular.contrib.rest_framework_simplejwt import SimpleJWTScheme
from rest_framework_simplejwt.authentication import JWTAuthentication


class CustomJWTAuthentication(JWTAuthentication):
    pass


class CustomJWTAuthenticationScheme(SimpleJWTScheme):
    target_class = 'config.auth.CustomJWTAuthentication'
    name = 'CustomJWTAuth'
