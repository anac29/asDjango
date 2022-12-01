from futbol import populateDB
from django.shortcuts import render, get_object_or_404
from .models import Temporada, Equipo, Partido, Jornada

# Create your views here.

def cargar(request):
    if populateDB.populateDatabase():
        tem=Temporada.objects.all().count()
        eq=Equipo.objects.all().count()
        part=Partido.objects.all().count()
        jor=Jornada.objects.all().count()
        info="Datos cargados correctamente"+"Temporadas"+str(tem)+"| Equipos"+str(eq)+"| Partidos"+str(part)+"| Jornadas"+str(jor)
    else:
        info="Error"

    return render(request, 'inicio.html', {'info':info})


def temporadas(request):
    nTem=Temporada.objects.all().count()
    info="Actualmente tenemos almacenadas"+str(nTem)+"temporadas."
    temporadas=Temporada.objects.all()
    return render(request, 'inicio.html', {'info':info, 'temporadas':temporadas})

def equipos(request):
    equipos=Equipo.objects.all()
    return render(request, 'equipos.html',{'datos':equipos})

def equipoDetalle(request,id_equipo):
    equipos=Equipo.objects.get_object_or_404(id=id_equipo)
    return render(request,'detalle.html',{'info':equipos})
    
def inicio(request):
    return render(request,'inicio.html')


