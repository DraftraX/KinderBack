from rest_framework import serializers
from .models import Usuario
from django.contrib.auth.models import User

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','password')