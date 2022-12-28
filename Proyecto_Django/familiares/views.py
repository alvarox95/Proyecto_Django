from django.shortcuts import render
from django.http import HttpResponse
from familiares.models import familiares
# Create your views here.
def create_familiar(request):
    familiares.objects.create(nombre="Ignacio Javier", apellido="Medici", edad=20, trabajador=True)
    return HttpResponse("Se agrego el nuevo Familiar")

def read_familiar(request):
    return render (request, 'read_familiar.html', context={})