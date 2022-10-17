from dataclasses import field
from rest_framework import serializers

from .models import Caracteristicas_Producto, Compra, Compra_Detalle, Inventariador, Inventario, Marca, Precio_Proveedor, Precio_ventas, Producto_Proveedor,Productos,Proveedor, Unidad_de_Medidas

class MarcaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Marca
        fields = '__all__'

class ProductosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Productos
        fields = '__all__'

class ProveedorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proveedor
        fields = '__all__'

class Producto_ProveedorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto_Proveedor
        fields = '__all__'

class Unidad_de_MedidasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Unidad_de_Medidas
        fields = '__all__'

class Precio_VentasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Precio_ventas
        fields = '__all__'

class Caracteristicas_ProdcutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Caracteristicas_Producto
        fields = '__all__'

class CompraSerializer(serializers.ModelSerializer):

    class Meta:
        model = Compra
        fields = '__all__'

class Precio_ProveedorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Precio_Proveedor
        fields = '__all__'

class Compra_DetalleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Compra_Detalle
        fields = '__all__'

class InventariadorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventariador
        fields = '__all__'

class InventarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventario
        fields = '__all__'