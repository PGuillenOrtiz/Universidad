from django.urls import path
from Aplicaciones.Academico.views import CursosListView, eliminar_curso, registrar_curso

urlpatterns = [
    path('', CursosListView.as_view(), name='gestion_cursos'),
    path('registrarCurso/', registrar_curso),
    path('eliminarCurso/<int:id>', eliminar_curso)
]