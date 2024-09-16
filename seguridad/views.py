from django.shortcuts import render
# from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UsuarioSerializer
from .models import Usuario

# class UsuarioView(viewsets.ModelViewSet):
#     serializers_class = UsuarioSerializer
#     queryset = Usuario.objects.all()
class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    permission_classes = [
        AllowAny
    ]
    serializer_class = UsuarioSerializer


# Create your views here.
