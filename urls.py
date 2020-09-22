from django.urls import path
from Proy1 import views
from Proy1.models import Negocio, Producto


urlpatterns = [
	
	path("login/", views.login),
	path("registro/", views.nuevo_registro),
	path("exito/", views.exito)
]