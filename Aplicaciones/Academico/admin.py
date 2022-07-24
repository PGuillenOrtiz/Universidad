from django.contrib import admin
from .models import Curso, Docentes

# Register your models here.
@admin.register(Curso)

class Curso(admin.ModelAdmin):
    list_display = ('id', 'coloreado', 'creditos')
    search_fields = ('nombre', 'creditos')

admin.site.register(Docentes)