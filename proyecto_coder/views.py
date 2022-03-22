from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime


def primer_vista(request):
    return HttpResponse("Hola Mundo desde mi primer vista en Django")

def segunda_vista(request):
    return HttpResponse("<h1>Titulo 1</h1> <p>Esto es un parrafo </p>")

def dia_hora(request):
    fecha_hora = datetime.now()
    return HttpResponse(f"<p>Tiempo actual: {fecha_hora}</p>")

def nombre_usuario(request, nombre):
    return HttpResponse(f"Tu nombre es {nombre}")

def edad_usuario(request, edad):
    anio_nacimiento = 2022 - int(edad)
    return HttpResponse(f"Usted tiene {anio_nacimiento} años")

def pagina_inicio(request):
    archivo = open(r"C:\Users\sebas\OneDrive\Documentos\Django_Intro\proyecto_coder\proyecto_coder\templates\page.html")
    
    plantilla = Template(archivo.read())

    archivo.close()

    context = Context()

    documento = plantilla.render(context)

    return HttpResponse(documento)