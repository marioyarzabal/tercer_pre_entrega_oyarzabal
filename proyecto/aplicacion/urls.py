from django.urls import path, include
from .views import *

urlpatterns = [
   path('', home, name="home"),
   path('clientes/', clientes, name="clientes"),
   path('proveedores/', proveedores, name="proveedores"),
   path('stock/', stock, name="stock"),
   path('cuentas/', cuentas, name="cuentas"),
   path('productos/', productos, name="productos"),

   ##__________________________________________________Formularios
   path('clientes_forms/', clientesForms, name="clientes_forms"),
   path('cuentas_forms/', cuentasForms, name="cuentas_forms"),
   path('proveedores_forms/', proveedoresForms, name="proveedores_forms"),
   path('productos_forms/', productosForms, name="productos_forms"),
   path('stocks_forms/', stockForms, name="stocks_forms"),
   
   ##__________________________________________________Formularios_Busqueda
   path('buscar/', buscar, name="buscar"),
   path('buscarClientes/', buscarClientes, name="buscarClientes"),
   path('buscarClientesNombre/', buscarClientesNombre, name="buscarClientesNombre"),

   path('buscarProductos/', buscarProductos, name="buscarProductos"),
   path('buscarproductosDroga/', buscarProductosDroga, name="buscarproductosDroga"),

   path('buscarProveedor/', buscarProveedor, name="buscarProveedor"),
   path('buscarProveedorCuit/', buscarProveedorCuit, name="buscarProveedorCuit"),

   path('buscarCuentas/', buscarCuentas, name="buscarCuentas"),
   path('buscarCuentasProducto/', buscarCuentasProducto, name="buscarCuentasProducto"),

   path('buscarStock/', buscarStock, name="buscarStock"),
   
   
]