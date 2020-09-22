from django.db import models

# Create your models here.

class Usuario(models.Model):
	usuario_id = models.IntegerField(primary_key = True, editable = False)
	email = models.EmailField(max_length = 254)
	contraseña = models.CharField(max_length = 20)

	def __str__(self):
		return self.nombre_usuario

class Negocio(models.Model):
	negocio_id = models.IntegerField(primary_key = True, editable = False)
	nombre = models.CharField(max_length = 60)
	rubro = models.CharField(max_length = 60)
	direccion = models.CharField(max_length = 100)
	localidad = models.CharField(max_length = 60)
	telefono = models.CharField(max_length = 30)
	email = models.EmailField(max_length = 254)
	contraseña = models.CharField(max_length = 20)
	red_social1 = models.URLField(max_length = 100, null = True)
	red_social2 = models.URLField(max_length = 100, null = True)
	red_social3 = models.URLField(max_length = 100, null = True)
	descripcion = models.TextField(null =True)
	usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre_negocio


class Producto(models.Model):
	id_producto = models.IntegerField(primary_key = True, editable = False)
	nombre = models.CharField(max_length = 60)
	precio = models.FloatField()
	descripcion = models.TextField(null=True)
	id_usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)


	def __str__(self):
		return self.nombre_producto
