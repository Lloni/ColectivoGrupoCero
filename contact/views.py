from django.shortcuts import render
from .forms import Contact

# contacto
def contacto(request):
    contact_form = Contact()
<<<<<<< HEAD

    # recuperando informacion de formulario
    if request.method == 'POST':
        contact_form = Contact(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('nombre_contacto')
            telefono = request.POST.get('telefono')
            email = request.POST.get('email')
            mensaje = request.POST.get('mensaje')
            imagen = request.POST.get('imagen')

            # envio de correo y redireccion
            email = EmailMessage(
                "Grupo Cero: Nuevo mensaje de contacto", # asunto
                "De {}, fono: {},correo <{}> \n \n Escribió: \n \n {} \n {}".format(name, telefono, email, mensaje, imagen), # cuerpo del mail
                "no_contestar@grupocero.cl", # email que emite
                ["mal.pozo@duocuc.cl"], # email de destino
                reply_to=[email] # responder al email de forma dinamica
            )

            try:
                email.send()
                return redirect(reverse('contacto')+"?ok")
            except:
                return redirect(reverse('contacto')+"?fail")


=======
>>>>>>> parent of 38d0f5a (models y formulario con django + envio de correo automatico)
    return render(request,"contact/contacto.html",{'form':contact_form})