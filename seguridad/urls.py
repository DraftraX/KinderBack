from django.urls import path, include
from rest_framework import routers
from .views import UsuarioViewSet


router = routers.DefaultRouter()
router.register('api/auth-login', UsuarioViewSet, basename='usuario')

urlpatterns = [
    path('', include(router.urls)),
]
