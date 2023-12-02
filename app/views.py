from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Estoy aprendiendo desde django')

def inicio(request):
    return render(request,'app/inicio.html')

def index(request,nombre):
    contexto={'nombre':nombre}
    return render(request,'app/index.html',contexto)

def equipo(request,num):
    contexto={'numero':num}
    return render(request,'app/equipo.html',contexto)