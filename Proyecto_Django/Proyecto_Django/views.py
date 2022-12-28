from django.http import HttpResponse
from django.shortcuts import render

def vista_con_template(request):
    return render(request,"index.html", context={}) 
