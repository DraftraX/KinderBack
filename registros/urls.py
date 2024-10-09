from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GradoViewSet, SeccionViewSet, AulaViewSet, AsistenciaViewSet, DocenteViewSet

# Crear un router y registrar los viewsets
router = DefaultRouter()
router.register(r'grados', GradoViewSet)
router.register(r'secciones', SeccionViewSet)
router.register(r'aulas', AulaViewSet)
router.register(r'asistencias', AsistenciaViewSet)
router.register(r'docentes', DocenteViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Incluir las URLs del router
]
