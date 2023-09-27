from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
    return render(request, "user/home.html")

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        passw = request.POST.get('pass')

        userLog = authenticate(username=username, password=passw)

        if userLog is not None:
            login(request, userLog)
            uName = userLog.username
            return redirect("http://127.0.0.1:8000/", {'uName': uName})

        else:
            messages.error(request, "Tus credenciales no coinciden")


    return render(request, "user/signin.html")

def signup(request):
    if request.method == "POST":
        uName = request.POST.get('username')
        uEmail1 = request.POST.get('email1')
        uEmail2 = request.POST.get('email2')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')



        if User.objects.filter(username=uName):
            messages.error(request, "Ese usuario no esta disponible")
            return redirect("http://127.0.0.1:8000/signin/")
        
        if User.objects.filter(email=uEmail1):
            messages.error(request, "Ese email ya esta en uso")
            return redirect("http://127.0.0.1:8000/signin/")
        
        if uEmail1 != uEmail2:
            messages.error(request, "Los emails no coinciden")
            return redirect("http://127.0.0.1:8000/signin/")

        if len(uName)>15:
            messages.error(request, "Tu nombre de usuario es demasiado largo (maximo 15 caracteres)")
            return redirect("http://127.0.0.1:8000/signin/")
        
        if User.objects.filter(email=uEmail1):
            messages.error(request, "Ese email ya esta en uso")
            return redirect("http://127.0.0.1:8000/signin/")
        
        if pass1 != pass2:
            messages.error(request, "Las contraseñas no coinciden")



        user = User.objects.create_user(uName, uEmail1, pass1)
        user.save()


        #Para enviar un email de bienvenida (mas adelante 55:52)

        messages.success(request, "Tu cuenta a sido creada exitosamente")
        
        return render(request, 'user/signin.html')
    
    return render(request, "user/signup.html")
 