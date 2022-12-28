from django.shortcuts import render
from django.http import HttpResponse
from familiares.models import familiares
# Create your views here.
def agregar_familiar(request):
    familiares.objects.create(nombre="Ignacio Javier", apellido="Medici", edad=20, trabajador=True)
    return HttpResponse("Se agrego el nuevo Familiar")

def listar_familia(request):
    lista_familiares = familiares.objects.all()
    context = {
        'familiares': familiares,
    }
    return render (request, 'listar_familia.html', context=context)