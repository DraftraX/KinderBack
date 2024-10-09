from rest_framework import serializers
from .models import Usuario, Modulo, Perfil, Acceso

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'  

class ModuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modulo
        fields = '__all__'  

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'  

class AccesoSerializer(serializers.ModelSerializer):
    modulo = serializers.PrimaryKeyRelatedField(queryset=Modulo.objects.all())
    perfil = serializers.PrimaryKeyRelatedField(queryset=Perfil.objects.all())

    class Meta:
        model = Acceso
        fields = '__all__' 
