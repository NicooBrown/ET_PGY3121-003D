from django.db import models
from django.core import validators

# Create your models here.

class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nombre_categoria = models.CharField(max_length=50,null=False)

    def __str__(self):
        txt = "ID : {1}-{0}"
        return txt.format(self.nombre_categoria,self.id_categoria)



class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50,null=False)
    precio = models.IntegerField(null=False)
    categoria_id = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    stock = models.IntegerField(null=False)
    descripcion = models.CharField(max_length=150 ,null=False)
    img_url = models.ImageField(upload_to='imagenesProducto', null=True)
    fecha_agregar = models.DateField(auto_now_add=True)

    def __str__(self):
        txt = "Codigo: {0} - Nombre: {1} - Categoria: {2} -  fecha: {3}"
        return txt.format(self.id_producto, self.nombre,self.categoria_id ,self.fecha_agregar)
    
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()
    numero_telefono = models.CharField(max_length=9)
    comentario = models.TextField()