from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def vista_con_template(request):
    return render(request,"index.html", context={}) 
