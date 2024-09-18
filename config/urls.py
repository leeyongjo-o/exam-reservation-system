from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularJSONAPIView, SpectacularRedocView

from config.views import HealthCheckView

urlpatterns = [
    path('admin/', admin.site.urls),

    # api docs
    path('swagger', SpectacularSwaggerView.as_view(url_name='schema'), name='schema'),
    path('swagger.json', SpectacularJSONAPIView.as_view(), name="schema"),
    path('redoc', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # health check
    path('ping', HealthCheckView.as_view(), name='health_check'),

    # test page auth
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]
