from django.shortcuts import render
# from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view



@api_view(['POST'])
def login (request):
    return Response({})

@api_view(['POST'])
def register(request):
    return Response({})

@api_view(['POST'])
def profile(request):
    return Response({})

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
