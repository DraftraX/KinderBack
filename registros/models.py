from django.db import models

class Grado(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        db_table = 'grados'


class Seccion(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        db_table = 'secciones'


class Aula(models.Model):
    capacidad = models.PositiveIntegerField(null=True, blank=True)
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    grado = models.ForeignKey(Grado, on_delete=models.SET_NULL, null=True)
    seccion = models.ForeignKey(Seccion, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'aulas'


class Asistencia(models.Model):
    estado = models.CharField(max_length=20)
    fecha = models.DateField()
    def get_alumno(self):
        from matricula.models import Alumno 
        alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)

    class Meta:
        db_table = 'asistencias'


class Docente(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    dni = models.CharField(max_length=8, unique=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    especialidad = models.CharField(max_length=100, null=True, blank=True)
    titulo_academico = models.CharField(max_length=100, null=True, blank=True)
    sexo = models.CharField(max_length=1, null=True, blank=True)  # M/F
    telefono = models.CharField(max_length=15, null=True, blank=True)
    fecha_contratacion = models.DateField(null=True, blank=True)
    estado = models.IntegerField(default=1)
    def get_Usuario(self):
        from seguridad.models import Usuario
        usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'docentes'