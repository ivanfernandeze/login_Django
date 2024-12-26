""" from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

# Create your views here.


def acceder(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect("home")
            else:
                messages.error(request, "los datos incorrectos")
        else:
            messages.error(request, 'datos incorrectos')
        form = AuthenticationForm()
        return render(request, "login.html", {"form": form})


def homePage(request):
    context = {}
    return render(request, "bienvenido.html", context)
 """

from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

# Create your views here.


def acceder(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect("home")
            else:
                messages.error(request, "Datos incorrectos")
        else:
            messages.error(request, "Datos incorrectos")
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


def homePage(request):
    context = {}
    return render(request, "layout/plantilla.html", context)


def tablas(request):
    return render(request, 'tablas.html', {})


def botones(request):
    return render(request, 'botones.html', {})
