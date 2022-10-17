
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from almacenkardex.views import caracteristicas_producto, compra, compra_detalle, inventariador, inventario, marca, precio_proveedor, precio_ventas, producto_proveedor, productos, proveedor, unidad_de_medidas

from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()

router.register('marcas',marca),
router.register('productos',productos),
router.register('proveedor',proveedor),
router.register('producto_proveedor',producto_proveedor),
router.register('unidad_de_medidas',unidad_de_medidas),
router.register('precio_ventas', precio_ventas),
router.register('caracteristicas_producto',caracteristicas_producto),
router.register('compra', compra),
router.register('precio_proveedor', precio_proveedor),
router.register('compra_detalle', compra_detalle),
router.register('inventariador', inventariador),
router.register('inventario', inventario)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
