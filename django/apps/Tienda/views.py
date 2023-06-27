from django.shortcuts import render, redirect
from .models import *
from django.conf import settings
import os
from django.http import HttpResponse
import json
from django import forms
from django.core.exceptions import ValidationError
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
import requests
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

# CARGA DE PÁGINAS
def cargarInicio(request):
    productos = Producto.objects.all()
    cate_games = Producto.objects.filter(categoria_id = 1)
    cate_steam = Producto.objects.filter(categoria_id = 2)
    return render(request, "inicio.html", {"prod":productos, "categoria_games": cate_games, "categoria_steam":cate_steam})

@permission_required('app.add_producto')
def cargarAgregarProducto(request):
    categorias  = Categoria.objects.all()
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 10)
        productos = paginator.page(page)
    except:
        raise Http404

    return render(request,"agregarProductos.html", {"cate":categorias, "prod":productos})

@permission_required('app.change_producto')
def cargarEditarProducto(request,id):

    producto = Producto.objects.get(id_producto = id)
    categorias = Categoria.objects.all()


    categoriaId = producto.categoria_id

    productoCategoriaId = Categoria.objects.get(id_categoria = categoriaId.id_categoria).id_categoria

    return render(request,"editarProducto.html",{"prod":producto,"cate":categorias, "categoriaId":productoCategoriaId})

def cargarContactanos(request):
    data = {
        'form': ContactoForm() 
    }

    if request.method  == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "¡Hemos recibido tu contacto con exito!"
        else:
            data["form"] = formulario

    return render(request, 'contactanos.html', data )
    


# FIN CARGA DE PÁGINAS


from django.contrib import messages


def agregarProducto(request):
    if request.method == 'POST':
        v_sku = request.POST['txtSku']
        v_nombre = request.POST['txtNombre']
        v_precio = request.POST['txtPrecio']
        v_stock = request.POST['txtStock']
        v_descripcion = request.POST['txtDescripcion']
        
        if not v_sku:
            return render(request, 'error.html', {'message': 'El campo SKU no puede estar vacío.'})
        
        if not v_nombre:
            return render(request, 'error.html', {'message': 'El campo Nombre no puede estar vacío.'})
        
        if not v_precio:
            return render(request, 'error.html', {'message': 'El campo Precio no puede estar vacío.'})
        
        if not v_stock:
            return render(request, 'error.html', {'message': 'El campo Stock no puede estar vacío.'})
        
        if not v_descripcion:
            return render(request, 'error.html', {'message': 'El campo Descripción no puede estar vacío.'})
        
        try:
            categoria = Categoria.objects.get(id_categoria=request.POST['cmbCategoria'])
        except Categoria.DoesNotExist:
            return render(request, 'error.html', {'message': 'La categoría seleccionada no existe.'})
        
        v_img = request.FILES.get('txtImg')
        
        try:
            producto = Producto.objects.create(
                id_producto=v_sku,
                nombre=v_nombre,
                precio=v_precio,
                stock=v_stock,
                descripcion=v_descripcion,
                img_url=v_img,
                categoria_id=categoria
            )
            messages.success(request, "Producto agregado de forma correcta")  # Agregar mensaje de éxito
        except ValidationError as e:
            return render(request, 'error.html', {'message': str(e)})
        
        return redirect('/agregarProducto')

    return render(request, 'agregar_producto.html')


@permission_required('app.change_producto')
def editarProducto(request):
    v_sku = request.POST['txtSku']
    productoBD = Producto.objects.get(id_producto=v_sku)
    v_nombre = request.POST['txtNombre']
    v_precio = request.POST['txtPrecio']
    v_stock = request.POST['txtStock']
    v_descripcion = request.POST['txtDescripcion']
    v_categoria = Categoria.objects.get(id_categoria=request.POST['cmbCategoria'])

    try:
        v_img = request.FILES['txtImg']
        ruta_imagen = os.path.join(settings.MEDIA_ROOT, str(productoBD.img_url))
        os.remove(ruta_imagen)
    except:
        v_img = productoBD.img_url

    productoBD.nombre = v_nombre
    productoBD.precio = v_precio
    productoBD.stock = v_stock
    productoBD.descripcion = v_descripcion
    productoBD.categoria_id = v_categoria
    productoBD.img_url = v_img

    productoBD.save()

    messages.success(request, "Modificado correctamente")

    return redirect('/agregarProducto')


@permission_required('app.delete_producto')
def eliminarProducto(request,id):
    producto = Producto.objects.get(id_producto = id)
    producto.delete()
    ruta_imagen  = os.path.join(settings.MEDIA_ROOT, str(producto.img_url))
    os.remove(ruta_imagen)
    messages.success(request, "Eliminado de manera correcta")
    return redirect('/agregarProducto')



def carritoVentas(request):
    #print("Productos Carrito------>",request.body)
    data = json.loads(request.body)
    for p in data:
        print("SKU",p['sku'])
        print("CANTIDAD",p['cantidad'])

    return HttpResponse("Goood!!!")

def registro(request):
    data = {
        'form': CustomCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="/")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)

def api(request):
    url = 'https://rickandmortyapi.com/api/character'
    response = requests.get(url)
    data = response.json()['results']
    personajes = []
    for personaje in data:
        personajes.append({
            'nombre': personaje['name'],
            'imagen': personaje['image'],
            'especie': personaje['species'],
            'estado': personaje['status'],
            'genero': personaje['gender'],
            'origen': personaje['origin']['name'],
            'ubicacion': personaje['location']['name']
        })
    return render(request, 'api.html', {'personajes': personajes})
