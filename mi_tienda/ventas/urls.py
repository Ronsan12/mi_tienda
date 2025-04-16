from django.urls import path
from . import views

urlpatterns = [
    path('', views.compras, name='compras'),
    path('categoria/<int:categoria_id>/', views.productos_por_categoria, name='productos_por_categoria'),
    path('shop/', views.shop, name='shop'),
    path('producto/<int:producto_id>/', views.product_detail, name='product_detail'),
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('incrementar/<int:item_id>/', views.incrementar_cantidad, name='incrementar_cantidad'),
    path('decrementar/<int:item_id>/', views.decrementar_cantidad, name='decrementar_cantidad'),
    path('eliminar/<int:item_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('comprar/', views.comprar_carrito, name='comprar_carrito'),
    path('obtener_cantidad_carrito/', views.obtener_cantidad_carrito, name='obtener_cantidad_carrito'),
    path('compras/', views.compras, name='compras'),
]
