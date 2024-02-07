from django import forms   

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
    tipo_producto=forms.CharField(max_length=100,required=True)
    limite_compra = forms.DecimalField(max_digits=10, decimal_places=2) 
    status=forms.BooleanField(required=True)

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
    