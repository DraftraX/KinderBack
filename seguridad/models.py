from django.db import models

# Create your models here.
class Usuario (models.Model):
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, blank=False, unique=True)
    estado = models.BooleanField(default=True)
    firsname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    numberphome = models.CharField(max_length=9)
    password = models.CharField(max_length=50, blank=False)
    username = models.CharField(max_length=50, blank=False)

    class Meta:
        db_table = "usuario"