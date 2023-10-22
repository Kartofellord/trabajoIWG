from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import userProfile
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import pycountry
import base64

# Create your views here.

def home(request):
    return render(request, "user/home.html")

 
def profile(request):
    if request.method == "POST":
        tipo = request.POST.get('tipo')
        pais = request.POST.get('pais')
        profesion = request.POST.get('profesion')
        biografia = request.POST.get('biografia')

        pic = request.FILES['pic']
        encoded = base64.b64encode(pic.read())
          
        profile = userProfile.objects.create(userClass = tipo,userPic = encoded.decode("utf-8"), userType = profesion,userCountry = pais, userBio = biografia,user = request.user)
        profile.save()

        return redirect("http://127.0.0.1:8000/profile/", {'profile':profile})

        #validar inputs


       

    all_countries = list(pycountry.countries)
    return render(request, "user/profile.html", {'countries':[country.name for country in all_countries]})



def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        passw = request.POST.get('pass')

        userLog = authenticate(username=username, password=passw)

        if userLog is not None:
            login(request, userLog)
            uName = userLog.get_username
            user_id = userLog.id
            print(user_id)
            return redirect("http://127.0.0.1:8000/", {'user':uName, 'user_id':user_id})

        else:
            messages.error(request, "Tu nombre de usuario o contraseña estan erroneos")
   
    
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
        
        if uEmail1 == "":
            messages.error(request, "Por favor ingresa un email valido")
            return redirect("http://127.0.0.1:8000/signin/")
        
        if uEmail1 != uEmail2:
            messages.error(request, "Los emails no coinciden")
            return redirect("http://127.0.0.1:8000/signin/")
        
        if uName == "":
            messages.error(request, "Por favor ingresa un nombre de usuario valido")
            return redirect("http://127.0.0.1:8000/signin/")

        elif len(uName)>15:
            messages.error(request, "Tu nombre de usuario es demasiado largo (maximo 15 caracteres)")
            return redirect("http://127.0.0.1:8000/signin/")
        
        if User.objects.filter(email=uEmail1):
            messages.error(request, "Ese email ya esta en uso")
            return redirect("http://127.0.0.1:8000/signin/")
        
        if pass1 == "":
            messages.error(request, "Por favor ingresa una contraseña valida")
            return redirect("http://127.0.0.1:8000/signin/")

        elif pass1 != pass2:
            messages.error(request, "Las contraseñas no coinciden")



        user = User.objects.create_user(uName, uEmail1, pass1)
        user.save()


        #Para enviar un email de bienvenida (mas adelante 55:52)

        messages.success(request, "Tu cuenta a sido creada exitosamente")
        
        return render(request, 'user/signin.html')
    
    return render(request, "user/signup.html")

def signout(request):
    logout(request)
    messages.success(request, "Cerraste sesión de forma exitosa")
    return redirect("http://127.0.0.1:8000/")
 