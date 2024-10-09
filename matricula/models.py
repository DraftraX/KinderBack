from django.db import models

class Apoderado(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    dni = models.CharField(max_length=8, unique=True)  # Dato común en Perú es de 8 dígitos
    email = models.EmailField(max_length=100, null=True, blank=True)
    estado = models.IntegerField(default=1)
    estado_civil = models.CharField(max_length=50, null=True, blank=True)
    ocupacion = models.CharField(max_length=100, null=True, blank=True)
    sexo = models.CharField(max_length=1, null=True, blank=True)  # M/F
    telefono = models.CharField(max_length=15, null=True, blank=True)

    class Meta:
        db_table = 'apoderados'


class Alumno(models.Model):
    
    apellidos = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    dni = models.CharField(max_length=8, unique=True)
    estado = models.IntegerField(default=1)
    estado_financiero = models.CharField(max_length=50, null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    lugar_nacimiento = models.CharField(max_length=100, null=True, blank=True)
    sexo = models.CharField(max_length=1, null=True, blank=True)  # M/F
    apoderado = models.ForeignKey(Apoderado, on_delete=models.SET_NULL, null=True)
    def get_aula(self):
        from registros.models import Aula 
        aula = models.ForeignKey(Aula, on_delete=models.SET_NULL, null=True)
    

    class Meta:
        db_table = 'alumnos'