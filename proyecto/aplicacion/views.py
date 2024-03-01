from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth.forms      import AuthenticationForm
from django.contrib.auth            import authenticate, login, logout
from django.contrib.auth.mixins     import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request,"aplicacion/home.html")

#_____________________________________________________________________Clientes
@login_required
def clientes(request):
    contexto = {'clientes': Cliente.objects.all()}
    return render(request,"aplicacion/clientes.html", contexto)

@login_required
def clientesForms(request):
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            id_cliente = miForm.cleaned_data.get("id_cliente")
            cliente_nombre = miForm.cleaned_data.get("nombre")
            cliente_apellido = miForm.cleaned_data.get("apellido")
            cliente_dni = miForm.cleaned_data.get("dni")
            cliente_fn = miForm.cleaned_data.get("fecha_nacimiento")
            cliente_domicilio = miForm.cleaned_data.get("domicilio")
            cliente_email = miForm.cleaned_data.get("email")
            cliente = Cliente(id_cliente=id_cliente,
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

@login_required
def updateCliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            cliente.id_cliente = miForm.cleaned_data.get('id_cliente')
            cliente.nombre = miForm.cleaned_data.get('nombre')
            cliente.apellido = miForm.cleaned_data.get('apellido')
            cliente.dni = miForm.cleaned_data.get('dni')
            cliente.fecha_nacimiento = miForm.cleaned_data.get('fecha_nacimiento') 
            cliente.domicilio = miForm.cleaned_data.get('domicilio') 
            cliente.email = miForm.cleaned_data.get('email') 
            cliente.save()
            return redirect(reverse_lazy('clientes'))   
    else:
        miForm = ClienteForm(initial={
            'id_cliente': cliente.id_cliente,
            'nombre': cliente.nombre,
            'apellido': cliente.apellido,
            'dni': cliente.dni,
            'fecha_nacimiento': cliente.fecha_nacimiento,
            'domicilio': cliente.domicilio,
            'email': cliente.email,
        })
    return render(request, "aplicacion/clientesForms.html", {'form': miForm})

@login_required
def deleteCliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.delete()
    return redirect(reverse_lazy('clientes'))

#_____________________________________________________________________Cuentas
@login_required
def cuentas(request):
    cuentas = Cuenta.objects.all()
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()

    #for c in cuentas:
     #   for j in productos:
      #      if c.id_producto==j.id_producto:
       #         total = c.cantidad_unidades*j.precio
    return render(request,"aplicacion/cuentas.html", {'cuentas': cuentas, 'productos': productos, 'clientes':clientes})

@login_required
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

@login_required
def updateCuenta(request, id):
    cuenta = Cuenta.objects.get(id=id)
    if request.method == "POST":
        miForm = CuentaForm(request.POST)
        if miForm.is_valid():
            cuenta.id_cliente = miForm.cleaned_data.get('id_cliente')
            cuenta.id_producto = miForm.cleaned_data.get('id_producto')
            cuenta.cantidad_unidades = miForm.cleaned_data.get('cantidad_unidades')
            cuenta.status = miForm.cleaned_data.get('status')
            cuenta.fecha_pago = miForm.cleaned_data.get('fecha_pago') 
            cuenta.fecha_compra = miForm.cleaned_data.get('fecha_compra') 
            cuenta.save()
            return redirect(reverse_lazy('cuentas'))   
    else:
        miForm = CuentaForm(initial={
            'id_cliente': cuenta.id_cliente,
            'id_producto': cuenta.id_producto,
            'cantidad_unidades': cuenta.cantidad_unidades,
            'status': cuenta.status,
            'fecha_pago': cuenta.fecha_pago,
            'fecha_compra': cuenta.fecha_compra,
        })
    return render(request, "aplicacion/cuentasForms.html", {'form': miForm})

@login_required
def deleteCuenta(request, id):
    cuenta = Cuenta.objects.get(id=id)
    cuenta.delete()
    return redirect(reverse_lazy('cuentas'))

#_____________________________________________________________________Proveedores

class ProveedorList(LoginRequiredMixin,ListView):
    model = Proveedor

class ProveedorCreate(LoginRequiredMixin, CreateView):
    model = Proveedor
    fields = ['id_proveedor', 'nombre', 'cuit','domicilio','email','tipo_producto','limite_compra','status']
    success_url = reverse_lazy('proveedores')


class ProveedorUpdate(LoginRequiredMixin,UpdateView):
    model = Proveedor
    fields = ['id_proveedor', 'nombre', 'cuit','domicilio','email','tipo_producto','limite_compra','status']
    success_url = reverse_lazy('proveedores')

class ProveedorDelete(LoginRequiredMixin,DeleteView):
    model = Proveedor
    success_url = reverse_lazy('proveedores')

#_____________________________________________________________________Stock

class StockList(LoginRequiredMixin,ListView):
    model = Stock

class StockCreate(LoginRequiredMixin, CreateView):
    model = Stock
    form_class = StockForm
    success_url = reverse_lazy('stock')

class StockUpdate(LoginRequiredMixin,UpdateView):
    model = Stock
    fields = ['id_producto', 'cantidad_unidades', 'min_unidades']
    success_url = reverse_lazy('stock')

class StockDelete(LoginRequiredMixin,DeleteView):
    model = Stock
    success_url = reverse_lazy('stock')

#_____________________________________________________________________Productos

class ProductoList(LoginRequiredMixin,ListView):
    model = Producto

class ProductoCreate(LoginRequiredMixin,CreateView):
    model = Producto
    form_class = ProductosForm
    success_url = reverse_lazy('productos')

class ProductoUpdate(LoginRequiredMixin,UpdateView):
    model = Producto
    fields = ['id_producto', 'id_proveedor', 'nombre','presentacion','fecha_elav','fecha_vence','droga','precio']
    success_url = reverse_lazy('productos')

class ProductoDelete(LoginRequiredMixin,DeleteView):
    model = Producto
    success_url = reverse_lazy('productos')

#_____________________________________________________________________Busquedas
@login_required
def buscar(request):
    return render(request, "aplicacion/buscar.html")

@login_required
def buscarClientes(request):
    if request.GET["buscar"]:
        key = request.GET["buscar"]
        clientes = Cliente.objects.filter(dni__icontains=key)
        contexto = {"clientes": clientes}
        return render(request, "aplicacion/clientes.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")

@login_required
def buscarClientesNombre(request):
    if request.GET["buscar"]:
        key = request.GET["buscar"]
        clientes = Cliente.objects.filter(nombre__icontains=key)
        contexto = {"clientes": clientes}
        return render(request, "aplicacion/clientes.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")

@login_required
def buscarProductos(request):
    if request.GET["buscar"]:
        key = request.GET["buscar"]
        productos = Producto.objects.filter(nombre__icontains=key)
        contexto = {"productos": productos}
        return render(request, "aplicacion/productos.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")

@login_required
def buscarProductosDroga(request):
    if request.GET["buscar"]:
        key = request.GET["buscar"]
        productos = Producto.objects.filter(droga__icontains=key)
        contexto = {"productos": productos}
        return render(request, "aplicacion/productos.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")

@login_required
def buscarProveedor(request):
    if request.GET["buscar"]:
        key = request.GET["buscar"]
        proveedor = Proveedor.objects.filter(nombre__icontains=key)
        contexto = {"proveedores": proveedor}
        return render(request, "aplicacion/proveedores.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")

@login_required
def buscarProveedorCuit(request):
    if request.GET["buscar"]:
        key = request.GET["buscar"]
        proveedor = Proveedor.objects.filter(cuit__icontains=key)
        contexto = {"proveedores": proveedor}
        return render(request, "aplicacion/proveedores.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")

@login_required
def buscarCuentas(request):
    if request.GET["buscar"]:
        key = request.GET["buscar"]
        cuentas = Cuenta.objects.filter(nombre__icontains=key)
        contexto = {"cuentas": cuentas}
        return render(request, "aplicacion/cuentas.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")

@login_required
def buscarCuentasProducto(request):
    if request.GET["buscar"]:
        key = request.GET["buscar"]
        cuentas = Cuenta.objects.filter(nombre__icontains=key)
        contexto = {"cuentas": cuentas}
        return render(request, "aplicacion/cuentas.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")

@login_required
def buscarStock(request):
    if request.GET["buscar"]:
        key = request.GET["buscar"]
        stocks = Stock.objects.filter(id_producto__icontains=key)
        contexto = {"object_list": stocks}
        return render(request, "aplicacion/stock_list.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")


#________________________________________________________ Login, Logout, Registracion

def custom_logout(request):
    logout(request)
    return redirect(reverse_lazy('home'))

def login_request(request):
    if request.method == "POST":
        usuario = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=usuario, password=password)
        if user is not None:
            login(request, user)
            #____ Avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            #__________________________________________

            return render(request, "aplicacion/home.html")
        else:
            return redirect(reverse_lazy('login'))
        
    miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form": miForm })    

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))

    else:    
        miForm = RegistroForm()

    return render(request, "aplicacion/registro.html", {"form": miForm })  

#___________________________________________________________________ Editar perfil de usuario

@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            user = User.objects.get(username=usuario)
            user.email = informacion['email']
            user.first_name = informacion['first_name']
            user.last_name = informacion['last_name']
            user.set_password(informacion['password1'])
            user.save()
            return render(request, "aplicacion/home.html")
    else:    
        form = UserEditForm(instance=usuario)

    return render(request, "aplicacion/editarPerfil.html", {"form": form }) 

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = User.objects.get(username=request.user)

            # ____ Para borrar el avatar viejo
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            # __________________________________
            avatar = Avatar(user=usuario, imagen=form.cleaned_data['imagen'])
            avatar.save()

            # ___________ Hago una url de la imagen en request
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request, "aplicacion/home.html")

    else:    
        form = AvatarForm()

    return render(request, "aplicacion/agregarAvatar.html", {"form": form })     

def acercademi(request):
    return render(request, "aplicacion/acercademi.html")  

