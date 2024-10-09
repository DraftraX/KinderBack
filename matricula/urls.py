from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ApoderadoViewSet, AlumnoViewSet

# Crear un router y registrar los viewsets
router = DefaultRouter()
router.register(r'apoderados', ApoderadoViewSet)
router.register(r'alumnos', AlumnoViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Incluir las URLs del router
]
