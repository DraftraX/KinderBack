from django.db import models

# Optimización de los modelos

class Usuario(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)  # Guardar el hash de la contraseña
    email = models.EmailField(max_length=100, null=True, blank=True)
    firstname = models.CharField(max_length=100, null=True, blank=True)
    lastname = models.CharField(max_length=100, null=True, blank=True)
    estado = models.IntegerField(default=1)
    address = models.CharField(max_length=255, null=True, blank=True)
    numberphone = models.CharField(max_length=15, null=True, blank=True)

    class Meta:
        db_table = 'usuario'


class Modulo(models.Model):
    nombre = models.CharField(max_length=100)  # Reducido el tamaño a 100 caracteres
    segmento = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField(max_length=255, null=True, blank=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = 'modulos'


class Perfil(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = 'perfiles'


class Acceso(models.Model):
    estado = models.IntegerField(default=1)
    modulo = models.ForeignKey(Modulo, on_delete=models.SET_NULL, null=True)
    perfil = models.ForeignKey(Perfil, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'accesos'
