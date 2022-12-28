from django.shortcuts import render
from django.http import HttpResponse
from familiares.models import familiares
# Create your views here.
def agregar_familiar(request):
    familiares.objects.create(nombre="Ignacio Javier", apellido="Medici", edad=20, trabajador=True, pariente="Hermano")
    return HttpResponse("Se agrego el nuevo Familiar")

def eliminar_familiar(request):
    familiares.objects.filter(nombre="").delete()
    return HttpResponse("Se elimino el Familiar")

def listar_familia(request):
    lista_familiares = familiares.objects.all()
    context = {
        'familiares': lista_familiares,
    }
    return render (request, 'listar_familia.html', context=context)