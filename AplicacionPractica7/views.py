from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,  AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import CatalogoForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def holamundo(request):
    return HttpResponse("Hola mundo")

def home(request):
    return render(request, "home.html")

def registro(request):
    if request.method =='GET':
        return render(request,"registro.html",{
            "form":UserCreationForm
        })
    else:
        req=request.POST
        if req['password1']==req['password2']:
            try:
                user = User.objects.create_user(
                    username=req['username'], password=req['password1']
                )
                user.save()
                login(request, user)
                return redirect('/')
            except  IntegrityError as ie:
                return render(request,"registro.html",{
                    "form":UserCreationForm,
                    "msg":"Usuario existente"
                })
            except Exception as e:
                return render(request,"registro.html",{
                    "form":UserCreationForm,
                    "msg":f"Error {e}"
                })
        else:
            return render(request,"registro.html",{
                "form":UserCreationForm,
                "msg":"favor de verificar la contraseña"
                })
    
def cerrarsesion(request):
    logout(request)
    return redirect('/')

def iniciarSesion(request):
    if request.method=="GET":
        return render(request,"login.html",{
            "form":AuthenticationForm
        })
    else:
        try:
            user=authenticate(request,
                            username=request.POST['username'],password=request.POST['password'])
            if user is not None:
                return redirect('/')
            else:
                return render(request,"login.html",{
                "form":AuthenticationForm,
                "msg":"Usuario o contraseña incorrectos"
            })
        except Exception as e:
            return render(request,"login.html",{
            "form":AuthenticationForm,
            "msg":f"Error {e}"
        })

@login_required
def nuevoCatalogo(request):
    if request.method=="GET":
        return render(request,"catalogo.html",{
                "form":CatalogoForm
            })
    else:
        try:
            form = CatalogoForm(request.POST)
            if form.is_valid():
                nuevo=form.save(commit=False)
                if request.user.is_authenticated:
                    nuevo.usuario=request.user
                    nuevo.save()
                    return redirect('/')
                else:
                    return render(request,"catalogo.html",{
                    "form":CatalogoForm,
                    "msg":"falta autenticacion"
                })
            else:
                return render(request,"catalogo.html",{
                    "form":CatalogoForm,
                    "msg":"formulario no valido"
                })
        except Exception as e:
            return render(request,"catalogo.html",{
                    "form":CatalogoForm,
                    "msg":f"Error {e}"
                })