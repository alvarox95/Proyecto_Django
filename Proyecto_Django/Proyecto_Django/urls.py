from django.contrib import admin
from django.urls import path
from Proyecto_Django.views import hola_mundo, vista_con_template
from familiares.views import create_familiar, read_familiar
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola/',hola_mundo ),
    path('vista-con-template/', vista_con_template),
    path('agregar-familiares/', create_familiar),
    path('leer-familiares/', read_familiar),
]
