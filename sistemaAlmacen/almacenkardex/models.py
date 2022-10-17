from django.db import models

# Create your models here.
class Marca(models.Model):
    marca = models.CharField(max_length=30)

    def __str__(self):
        return self.marca

class Productos(models.Model):
    producto = models.CharField(max_length=50)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.producto

class Proveedor(models.Model):
    proveedor = models.CharField(max_length=50)
    ruc = models.CharField(max_length=11)
    direcion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.CharField(max_length=30)

    def __str__(self):
       return self.proveedor

class Producto_Proveedor(models.Model):
     producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
     proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

     def __str__(self):
        return self.producto.producto + " / " + str(self.proveedor)

class Unidad_de_Medidas(models.Model):
    tipo_cantidad = models.CharField(max_length=25)

    def __str__(self):
       return self.tipo_cantidad

class Precio_ventas(models.Model):
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    preciov = models.DecimalField(max_digits=12,decimal_places=2)

    def __str__(self):
       return str(self.preciov) + " " + str(self.producto)

class Caracteristicas_Producto(models.Model):
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    caracteristica = models.CharField(default='',max_length=50)

    def __str__(self):
       return self.producto.producto


class Compra(models.Model):
    comprobante=models.CharField(max_length=20)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    preciot = models.DecimalField(default=0,max_digits=12,decimal_places=2)

    def __str__(self):
        return self.comprobante + " " + str(self.proveedor)

class Precio_Proveedor(models.Model):
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    preciop = models.DecimalField(max_digits=12,decimal_places=2)

    def __str__(self):
       return str(self.preciop) + " " + str(self.producto)

class Compra_Detalle(models.Model):
    compra= models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto_proveedor = models.ForeignKey(Producto_Proveedor, on_delete=models.CASCADE)
    cantidadt= models.DecimalField(default=0,max_digits=12,decimal_places=2)
    precio_unitario = models.DecimalField(max_digits=12,decimal_places=2) 
    preciop = models.ForeignKey(Precio_Proveedor, on_delete=models.CASCADE)
    subtotal= models.DecimalField(max_digits=12,decimal_places=2)

    def __str__(self):
       return str(self.producto_proveedor) + " - " + str(self.subtotal)

class Inventariador(models.Model):
    codigo_trabajador = models.CharField(max_length=10)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)

    def __str__(self):
       return str(self.nombres) + "  " + str(self.apellidos)

class Inventario(models.Model):
    fecha_horas = models.DateTimeField(auto_now_add=True)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    movimiento = models.CharField(max_length=1)
    compra_detalle = models.ForeignKey(Compra_Detalle, on_delete=models.CASCADE)
    stock = models.DecimalField(max_digits=12,decimal_places=2)
    inventariador = models.ForeignKey(Inventariador, on_delete=models.CASCADE,blank=True)

    def __str__(self):
       return str(self.producto) + " - " + str(self.movimiento)

