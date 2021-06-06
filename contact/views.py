from django.shortcuts import render
from .forms import Contact

# contacto
def contacto(request):
    contact_form = Contact()
    return render(request,"contact/contacto.html",{'form':contact_form})