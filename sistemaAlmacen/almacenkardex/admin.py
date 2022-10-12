from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Compra)
admin.site.register(models.Compra_Detalle)
admin.site.register(models.Inventario)
admin.site.register(models.Marca)
admin.site.register(models.Productos)
admin.site.register(models.Producto_Proveedor)
admin.site.register(models.Proveedor)
admin.site.register(models.Caracteristicas_Producto)
admin.site.register(models.Unidad_de_Medidas)
admin.site.register(models.Invetariador)
admin.site.register(models.Precio_ventas)
admin.site.register(models.Precio_Proveedor)
