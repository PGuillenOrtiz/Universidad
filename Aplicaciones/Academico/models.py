from django.db import models
from django.utils.html import format_html
from .choices import Sexo

# Create your models here.
class Docentes(models.Model):
    apellido_paterno = models.CharField(max_length=20, verbose_name='apellido_paterno')
    apellido_materno = models.CharField(max_length=20, verbose_name='apellido_materno')
    nombre = models.CharField(max_length=20, verbose_name='nombre')
    fecha_nacimiento = models.DateField(verbose_name='fecha de nacimiento')
    sexo = models.CharField(max_length=1, choices=Sexo, default='F')

    def nombre_completo(self):
        return '{} {}, {}'.format(self.apellido_paterno, self.apellido_materno, self.nombre)

    def __str__(self):
        return self.nombre_completo()

    class Meta:
        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'
        db_table = 'docente'
        ordering =['apellido_paterno', '-apellido_materno']

class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveSmallIntegerField()
    docente = models.ForeignKey(Docentes, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

    def coloreado(self):
        return format_html('<spam style="color:blue">{0}</spam>'.format(self.nombre))