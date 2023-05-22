from django.db import models

# Create your models here.
class Proveedor(models.Model):
    nombre=models.CharField(max_length=60)
    apellido=models.CharField(max_length=60)
    dni=models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nombre} - {self.apellido}"


class Producto(models.Model):
   nombre=models.CharField(max_length=60)
   precio=models.FloatField(default=0)
   stock_actual=models.IntegerField(default=0)
   proveedor=models.ForeignKey(
       Proveedor,
       related_name="productos",
       on_delete=models.CASCADE,

   )

   def __str__(self):
       return f"{self.nombre} - {self.proveedor}"
   #prueba