from django import forms   
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Stock, Producto, Proveedor

class ClienteForm(forms.Form):
    id_cliente=forms.IntegerField(required=True)
    nombre = forms.CharField(max_length=100, required=True)
    apellido = forms.CharField(max_length=100, required=True)
    dni=forms.IntegerField(required=True)
    fecha_nacimiento= forms.DateField(required=True)
    domicilio=forms.CharField(max_length=300, required=True)
    email=forms.EmailField(required=False)

class CuentaForm(forms.Form):
    id_cliente=forms.IntegerField(required=True)
    id_producto=forms.IntegerField(required=True)
    cantidad_unidades=forms.IntegerField(required=True)
    status=forms.CharField(max_length=10,required=True)  #pagado/debe
    fecha_pago=forms.DateField(required=False) 
    fecha_compra=forms.DateField(required=True)

class ProveedoresForm(forms.Form):
    id_proveedor=forms.IntegerField(required=True)
    nombre = forms.CharField(max_length=100,required=True)
    cuit=forms.IntegerField(required=True)
    domicilio=forms.CharField(max_length=300,required=True)
    email=forms.EmailField()
    tipo_producto = forms.CharField(max_length=100,required=True)
    limite_compra = forms.DecimalField(max_digits=10, decimal_places=2) 
    status=forms.BooleanField(required=True)

class ProveedoresForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['id_proveedor', 'nombre', 'cuit', 'domicilio', 'email', 'tipo_producto', 'limite_compra', 'status']
        widgets = {
            'tipo_producto': forms.Select(choices=Proveedor.TIPO_PRODUCTO_CHOICES)
        }

class ProductosForm(forms.Form):
    id_producto=forms.IntegerField()
    id_proveedor=forms.IntegerField()
    nombre = forms.CharField(max_length=100)
    presentacion = forms.CharField(max_length=100)
    fecha_elav= forms.DateField()
    fecha_vence= forms.DateField()
    droga=forms.CharField(max_length=300)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)

class StockForm(forms.Form):
    id_producto=forms.IntegerField(required=True)
    cantidad_unidades=forms.IntegerField()
    min_unidades = forms.IntegerField()
    
class RegistroForm(UserCreationForm):
    email = forms.EmailField(max_length=50, required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserEditForm(UserCreationForm):
    email = forms.EmailField(max_length=50, required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=True)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['id_producto', 'cantidad_unidades', 'min_unidades']

    def __init__(self, *args, **kwargs):
        super(StockForm, self).__init__(*args, **kwargs)
        productos = Producto.objects.all()
        choices = [(producto.id_producto, producto.nombre) for producto in productos]
        self.fields['id_producto'] = forms.ChoiceField(choices=choices)

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['id_producto', 'id_proveedor', 'nombre','presentacion','fecha_elav','fecha_vence','droga','precio']

    def __init__(self, *args, **kwargs):
        super(ProductosForm, self).__init__(*args, **kwargs)
        proveedores = Proveedor.objects.all()
        choices = [(proveedor.id_proveedor, proveedor.nombre) for proveedor in proveedores]
        self.fields['id_proveedor'] = forms.ChoiceField(choices=choices)
    
    