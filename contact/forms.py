from django import forms

class Contact(forms.Form):
    nombre_contacto = forms.CharField(max_length=20,label='Nombre y Apellido', required=True)
    telefono = forms.CharField(max_length=9, label='Telefono', required=True)
    email = forms.EmailField(max_length=30, label='E-mail', required=True)
    mensaje = forms.CharField(max_length=300, label='Mensaje', required=True, widget=forms.Textarea)
    imagen = forms.ImageField(label='Imagen', required=False)

