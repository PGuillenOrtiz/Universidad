from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.views.generic import ListView
from .models import Curso

# Create your views here.

def home(request):
    cursosListado = Curso.objects.all()
    #return HttpResponse("<h>Hola mundo</h>")
    #cursosListado = Curso.objects.filter(creditos__lte=5)

    data = {
        'titulo' : 'Gestion de mis Cursos',
        'cursos' : cursosListado
    }
    #return render(request, 'gestioncursos.html',{"cursos":cursosListado})
    return render(request, 'gestioncursos.html',data)

class CursosListView(ListView):
    model = Curso
    template_name = 'gestioncursos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Gestion de Curso'
        return context

def registrar_curso(request):
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']
    curso = Curso.objects.create(nombre=nombre, creditos=creditos)

    return redirect('/')

def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()

    return redirect('/')
