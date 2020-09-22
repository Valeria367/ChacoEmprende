from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from Proy1.models import Usuario, Negocio, Producto

# Create your views here.

def login(request):
	if request.method == "POST":
		datos = Usuario(request.POST)
		return HttpResponseRedirect('http://http://127.0.0.1:8000/Proy1/registro/')
	else:
		datos = Usuario
		context = {"value":datos}
	return render(request, "registro.html", context)


def nuevo_registro(request):
	if request.POST:
		post = request.POST
		nuevo_usuario = Negocio(post['nombre'], post['direccion'], post['telefono'], post['email'], post['contraseña'],post['red_social1'], post['red_social2'], post['red_social3'])
		nuevo_producto = Producto(post['precio'], post['descripcion'])
		nuevo_usuario.save()
		nuevo_producto.save()

	return render(request, "registro.html")


def exito(request):
	html = '<html><body><font color="green" size="4" face="Comic Sans MS, Arial, MS Sans Serif"><i><big>"¡Registro Exitoso!"</big></i></font></body></html>'
	return HttpResponse(html)

