from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
   path('', home, name="home"),
   path('clientes/', clientes, name="clientes"),
   path('cuentas/', cuentas, name="cuentas"),

##__________________________________________________CVV
   path('stock/', StockList.as_view(), name="stock"),
   path('stock_create/', StockCreate.as_view(), name="stock_create"),
   path('stock_update/<int:pk>/', StockUpdate.as_view(), name="stock_update"),
   path('stock_delete/<int:pk>/', StockDelete.as_view(), name="stock_delete"),

   path('productos/', ProductoList.as_view(), name="productos"),
   path('producto_create/', ProductoCreate.as_view(), name="producto_create"),
   path('producto_update/<int:pk>/', ProductoUpdate.as_view(), name="producto_update"),
   path('producto_delete/<int:pk>/', ProductoDelete.as_view(), name="producto_delete"),

   path('proveedores/', ProveedorList.as_view(), name="proveedores"),
   path('proveedores_create/', ProveedorCreate.as_view(), name="proveedores_create"),
   path('proveedores_update/<int:pk>/', ProveedorUpdate.as_view(), name="proveedores_update"),
   path('proveedores_delete/<int:pk>/', ProveedorDelete.as_view(), name="proveedores_delete"),
   
   ##__________________________________________________Formularios
   path('clientes_forms/', clientesForms, name="clientes_forms"),
   path('cuentas_forms/', cuentasForms, name="cuentas_forms"),
   
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

   ##______________________________________________________________________________CRUDS
   path('clienteActualizar/<id_cliente>/', updateCliente, name="clienteActualizar"),
   path('clienteBorrar/<id_cliente>/', deleteCliente, name="clienteBorrar"),

   path('cuentaActualizar/<id>/', updateCuenta, name="cuentaActualizar"),
   path('cuentaBorrar/<id>/', deleteCuenta, name="cuentaBorrar"),
   
   #____________________________________________________ login, logout, registro
    path('login/', login_request, name="login"),
    path('registro/', register, name="registro"),
    #path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout"),
    path('logout/', custom_logout, name="logout"),
    path('editar_perfil/', editarPerfil, name="editar_perfil"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),
    path('acercademi/', acercademi, name="acercademi"),
]
    