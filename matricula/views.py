from rest_framework import viewsets
from .models import Apoderado, Alumno
from .serializers import ApoderadoSerializer, AlumnoSerializer

class ApoderadoViewSet(viewsets.ModelViewSet):
    queryset = Apoderado.objects.all()
    serializer_class = ApoderadoSerializer

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
