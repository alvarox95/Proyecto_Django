from django.contrib import admin
from django.urls import path
from familiares.views import agregar_familiar, listar_familia, eliminar_familiar
urlpatterns = [
    path('admin/', admin.site.urls),
    path('agregar-familiares/', agregar_familiar),
    path('leer-familiares/', listar_familia),
    path('eliminar-familiares/', eliminar_familiar),
]
