from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, ModuloViewSet, PerfilViewSet, AccesoViewSet

# Crear un router y registrar los viewsets
router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'modulos', ModuloViewSet)
router.register(r'perfiles', PerfilViewSet)
router.register(r'accesos', AccesoViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Incluir las URLs del router
]
