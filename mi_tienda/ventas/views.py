from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Producto, Categoria, Carrito, ItemCarrito
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'ventas/home.html')

def productos_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    productos = Producto.objects.filter(categoria=categoria)   
    tamaño_seleccionado = request.GET.get('tamaño', '')
    categorias = Categoria.objects.all()
    paginator = Paginator(productos, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'ventas/productos_por_categoria.html', {'tamaño_seleccionado': tamaño_seleccionado,'productos': page_obj, 'categorias': categorias, 'categoria_seleccionada': categoria})

def compras(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    
    tamaño = request.GET.get('tamaño')
    if tamaño:
        productos = productos.filter(tamaño=tamaño)
        
    paginator = Paginator(productos, 6)  # Mostrar 6 productos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'categorias': categorias,
        'productos': page_obj,
        'tamaño_seleccionado': tamaño  # Pasar el tamaño seleccionado al contexto
    }
    
    return render(request, 'ventas/compras.html', context)

def contacto(request):
    return render(request, 'ventas/contacto.html')

def nosotros(request):
    return render(request, 'ventas/nosotros.html')

def shop(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    return render(request, 'ventas/shop.html', {'categorias': categorias, 'productos': productos})

def product_detail(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'ventas/shop.html', {'producto': producto})


@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user, defaults={'creado_en': timezone.now()})
    item, created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    
    if not created:
        item.cantidad += 1
        item.save()
    
    return redirect('ver_carrito')

@login_required
def ver_carrito(request):
    carrito = Carrito.objects.filter(usuario=request.user).first()
    items = ItemCarrito.objects.filter(carrito=carrito)
    return render(request, 'ventas/carrito.html', {'carrito': carrito, 'items': items})

@login_required
def incrementar_cantidad(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id)
    item.cantidad += 1
    item.save()
    return redirect('ver_carrito')

@login_required
def decrementar_cantidad(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id)
    if item.cantidad > 1:
        item.cantidad -= 1
    else:
        item.delete()
    item.save()
    return redirect('ver_carrito')

@login_required
def eliminar_del_carrito(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id)
    item.delete()
    return redirect('ver_carrito')

@login_required
def comprar_carrito(request):
    carrito = Carrito.objects.filter(usuario=request.user).first()
    if carrito:
        items = ItemCarrito.objects.filter(carrito=carrito)
        # Aquí puedes agregar la lógica de procesamiento de la compra
        carrito.delete()
        messages.success(request, "Compra realizada con éxito.")
    return redirect('compras')


@login_required
def obtener_cantidad_carrito(request):
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    total_items = sum(item.cantidad for item in carrito.items.all())
    return JsonResponse({'total': total_items})


