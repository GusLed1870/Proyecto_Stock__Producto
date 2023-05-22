from django.contrib import admin
from compra_app.models import Proveedor, Producto

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    model=Producto
    list_display=("id","nombre","precio","stock_actual","proveedor")
    search_fields=("nombre","proveedor__nombre")
    list_filter=("proveedor__nombre",) #filtra por proveedor

class ProveedorAdmin(admin.ModelAdmin):
    model=Proveedor
    list_display=("id","nombre","apellido")
    search_fields=("nombre",)  

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
