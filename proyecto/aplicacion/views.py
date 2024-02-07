from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request,"aplicacion/home.html")

#_____________________________________________________________________Clientes
def clientes(request):
    contexto = {'clientes': Cliente.objects.all()}
    return render(request,"aplicacion/clientes.html", contexto)

def clientesForms(request):
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            cliente_id = miForm.cleaned_data.get("id_cliente")
            cliente_nombre = miForm.cleaned_data.get("nombre")
            cliente_apellido = miForm.cleaned_data.get("apellido")
            cliente_dni = miForm.cleaned_data.get("dni")
            cliente_fn = miForm.cleaned_data.get("fecha_nacimiento")
            cliente_domicilio = miForm.cleaned_data.get("domicilio")
            cliente_email = miForm.cleaned_data.get("email")
            cliente = Cliente(id_cliente=cliente_id,
                              nombre=cliente_nombre, 
                              apellido = cliente_apellido, 
                              dni=cliente_dni,
                              fecha_nacimiento=cliente_fn,
                              domicilio=cliente_domicilio,
                              email=cliente_email)
            cliente.save()
            return redirect(reverse_lazy('clientes'))

    else:    
        miForm = ClienteForm()

    return render(request, "aplicacion/clientesForms.html", {"form": miForm })

#_____________________________________________________________________Proveedores
def proveedores(request):
    contexto = {'proveedores': Proveedor.objects.all()}
    return render(request,"aplicacion/proveedores.html", contexto)

def proveedoresForms(request):
    if request.method == "POST":
        miForm = ProveedoresForm(request.POST)
        if miForm.is_valid():
            prov_id = miForm.cleaned_data.get("id_proveedor")
            prov_nombre = miForm.cleaned_data.get("nombre")
            prov_cuit = miForm.cleaned_data.get("cuit")
            prov_domicilio = miForm.cleaned_data.get("domicilio")
            prov_email = miForm.cleaned_data.get("email")
            prov_tipo_prod = miForm.cleaned_data.get("tipo_producto")
            prov_limite_com = miForm.cleaned_data.get("limite_compra")
            prov_status = miForm.cleaned_data.get("status")
            
            proveedor = Proveedor(id_proveedor=prov_id,
                              nombre=prov_nombre, 
                              cuit = prov_cuit, 
                              domicilio=prov_domicilio,
                              email=prov_email,
                              tipo_producto=prov_tipo_prod,
                              limite_compra=prov_limite_com,
                              status=prov_status)
            proveedor.save()
            return redirect(reverse_lazy('proveedores'))

    else:    
        miForm = ProveedoresForm()

    return render(request, "aplicacion/proveedoresForms.html", {"form": miForm })

#_____________________________________________________________________Cuentas
def cuentas(request):
    cuentas = Cuenta.objects.all()
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()

    #for c in cuentas:
     #   for j in productos:
      #      if c.id_producto==j.id_producto:
       #         total = c.cantidad_unidades*j.precio
    return render(request,"aplicacion/cuentas.html", {'cuentas': cuentas, 'productos': productos, 'clientes':clientes})

def cuentasForms(request):
    if request.method == "POST":
        miForm = CuentaForm(request.POST)
        contexto = {"cuentas": cuentas }
        if miForm.is_valid():
            cuenta_id = miForm.cleaned_data.get("id_cliente")
            cuenta_prod = miForm.cleaned_data.get("id_producto")
            cuenta_qunid = miForm.cleaned_data.get("cantidad_unidades")
            cuenta_status = miForm.cleaned_data.get("status")
            cuenta_fp = miForm.cleaned_data.get("fecha_pago")
            cuenta_fc = miForm.cleaned_data.get("fecha_compra")
            cuenta = Cuenta(id_cliente=cuenta_id,
                              id_producto=cuenta_prod, 
                              cantidad_unidades = cuenta_qunid, 
                              status=cuenta_status,
                              fecha_pago=cuenta_fp,
                              fecha_compra=cuenta_fc)
            cuenta.save()
            return redirect(reverse_lazy('cuentas'))

    else:    
        miForm = CuentaForm()

    return render(request, "aplicacion/cuentasForms.html", {"form": miForm })

#_____________________________________________________________________Stock
def stock(request):
    contexto = {'stock': Stock.objects.all()}
    return render(request,"aplicacion/stock.html", contexto)

def stockForms(request):
    if request.method == "POST":
        miForm = StockForm(request.POST)
        if miForm.is_valid():
            stock_prod_id = miForm.cleaned_data.get("id_producto")
            stock_qa = miForm.cleaned_data.get("cantidad_unidades")
            stock_qmin = miForm.cleaned_data.get("min_unidades")
                      
            stock = Stock(id_producto=stock_prod_id, 
                          cantidad_unidades = stock_qa, 
                          min_unidades=stock_qmin)
                             
            stock.save()
            return redirect(reverse_lazy('stock'))

    else:    
        miForm = StockForm()

    return render(request, "aplicacion/stockForms.html", {"form": miForm })

#_____________________________________________________________________Productos
def productos(request):
    contexto = {'productos': Producto.objects.all()}
    return render(request,"aplicacion/productos.html", contexto)

def productosForms(request):
    if request.method == "POST":
        miForm = ProductosForm(request.POST)
        if miForm.is_valid():
            prod_id = miForm.cleaned_data.get("id_producto")
            prod_id_prov = miForm.cleaned_data.get("id_proveedor")
            prod_nombre = miForm.cleaned_data.get("nombre")
            prod_presentacion = miForm.cleaned_data.get("presentacion")
            prod_fe = miForm.cleaned_data.get("fecha_elav")
            prod_fv = miForm.cleaned_data.get("fecha_vence")
            prod_droga = miForm.cleaned_data.get("droga")
            prod_precio = miForm.cleaned_data.get("precio")
            
            producto = Producto(id_producto=prod_id,
                              id_proveedor=prod_id_prov, 
                              nombre = prod_nombre, 
                              presentacion=prod_presentacion,
                              fecha_elav=prod_fe,
                              fecha_vence=prod_fv,
                              droga=prod_droga,
                              precio=prod_precio)
            producto.save()
            return redirect(reverse_lazy('productos'))

    else:    
        miForm = ProductosForm()

    return render(request, "aplicacion/productosForms.html", {"form": miForm })

#_____________________________________________________________________Busquedas
def buscar(request):
    return render(request, "aplicacion/buscar.html")

def buscarClientes(request):
    if request.GET["buscar"]:
        key = request.GET["buscar"]
        clientes = Cliente.objects.filter(dni__icontains=key)
        #    clientes = Cliente.objects.filter(nombre__icontains=key)
        contexto = {"clientes": clientes}
        return render(request, "aplicacion/clientes.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")

def buscarClientesNombre(request):
    if request.GET["buscar"]:
        key = request.GET["buscar"]
        clientes = Cliente.objects.filter(nombre__icontains=key)
        contexto = {"clientes": clientes}
        return render(request, "aplicacion/clientes.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")

def buscarProductos(request):
    if request.GET["buscar"]:
        key = request.GET["buscar"]
        productos = Producto.objects.filter(nombre__icontains=key)
        contexto = {"productos": productos}
        return render(request, "aplicacion/productos.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")

def buscarProductosDroga(request):
    if request.GET["buscar"]:
        key = request.GET["buscar"]
        productos = Producto.objects.filter(droga__icontains=key)
        contexto = {"productos": productos}
        return render(request, "aplicacion/productos.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")

def buscarProveedor(request):
    if request.GET["buscar"]:
        key = request.GET["buscar"]
        proveedor = Proveedor.objects.filter(nombre__icontains=key)
        contexto = {"proveedores": proveedor}
        return render(request, "aplicacion/proveedores.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")

def buscarProveedorCuit(request):
    if request.GET["buscar"]:
        key = request.GET["buscar"]
        proveedor = Proveedor.objects.filter(cuit__icontains=key)
        contexto = {"proveedores": proveedor}
        return render(request, "aplicacion/proveedores.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")

def buscarCuentas(request):
    if request.GET["buscar"]:
        key = request.GET["buscar"]
        cuentas = Cuenta.objects.filter(nombre__icontains=key)
        contexto = {"cuentas": cuentas}
        return render(request, "aplicacion/cuentas.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")

def buscarCuentasProducto(request):
    if request.GET["buscar"]:
        key = request.GET["buscar"]
        cuentas = Cuenta.objects.filter(nombre__icontains=key)
        contexto = {"cuentas": cuentas}
        return render(request, "aplicacion/cuentas.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")

def buscarStock(request):
    if request.GET["buscar"]:
        key = request.GET["buscar"]
        stocks = Stock.objects.filter(id_producto__icontains=key)
        contexto = {"stock": stocks}
        return render(request, "aplicacion/stock.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")