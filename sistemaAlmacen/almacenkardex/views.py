from django.shortcuts import render

from rest_framework import viewsets

from .models import Caracteristicas_Producto, Compra, Compra_Detalle,Inventario, Inventariador, Marca, Precio_Proveedor, Precio_ventas, Producto_Proveedor, Productos, Proveedor, Unidad_de_Medidas
from .serializers import Caracteristicas_ProdcutoSerializer, Compra_DetalleSerializer, CompraSerializer, InventariadorSerializer, InventarioSerializer, MarcaSerializer, Precio_ProveedorSerializer, Precio_VentasSerializer, ProductosSerializer, ProveedorSerializer, Unidad_de_MedidasSerializer,Producto_ProveedorSerializer
# Create your views here.


class marca(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class productos(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer

class proveedor(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class producto_proveedor(viewsets.ModelViewSet):
    queryset = Producto_Proveedor.objects.all()
    serializer_class = Producto_ProveedorSerializer

class unidad_de_medidas(viewsets.ModelViewSet):
    queryset = Unidad_de_Medidas.objects.all()
    serializer_class = Unidad_de_MedidasSerializer

class precio_ventas(viewsets.ModelViewSet):
    queryset = Precio_ventas.objects.all()
    serializer_class = Precio_VentasSerializer

class caracteristicas_producto(viewsets.ModelViewSet):
    queryset = Caracteristicas_Producto.objects.all()
    serializer_class = Caracteristicas_ProdcutoSerializer

class compra(viewsets.ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

class precio_proveedor(viewsets.ModelViewSet):
    queryset = Precio_Proveedor.objects.all()
    serializer_class = Precio_ProveedorSerializer

class compra_detalle(viewsets.ModelViewSet):
    queryset = Compra_Detalle.objects.all()
    serializer_class = Compra_DetalleSerializer

class inventariador(viewsets.ModelViewSet):
    queryset = Inventariador.objects.all()
    serializer_class = InventariadorSerializer

class inventario(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer


