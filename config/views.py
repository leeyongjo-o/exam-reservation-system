from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class HealthCheckView(APIView):
    permission_classes = [AllowAny, ]
    renderer_classes = [JSONRenderer, ]

    @extend_schema(exclude=True)
    def get(self, request, format=None):
        return Response('SUCCESS')
