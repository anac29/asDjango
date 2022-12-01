#encoding:utf-8
#IMPORTAR TABLAS DESDE EL MODELO

from bs4 import BeautifulSoup
import urllib.request
import re

TEMP_INI = 2019 # temporada inicial a cargar
NUM_TEMP = 3 # número de temporadas

def populateDatabase():
    
    #BORRAR TABLAS
    
    #cargamos NUM_TEMP temporadas desde la TEMP_INI
    temporadas = [str(TEMP_INI+t)+'_'+str(TEMP_INI+t+1) for t in range(0,NUM_TEMP)]

    for temporada in temporadas:
        
        #CREAMOS LA TEMPORADA
        
        for numero in range(1,39): #numero de jornada
            f = urllib.request.urlopen("http://resultados.as.com/resultados/futbol/primera/"+str(temporada)+"/jornada/regular_a_"+str(numero))
            s = BeautifulSoup(f,"lxml")
            fecha = s.find("span", class_=["fecha-evento"]).string.strip()

            #CREAMOS LA JORNADA


            partidos = s.find_all("li",class_='list-resultado')
            for p in partidos:
                equipos= p.find_all("span",class_="nombre-equipo")
                
                nombre_local = equipos[0].string.strip().lower()
                link_local = equipos[0].parent['href']
                #CREAMOS EL EQUIPO SI NO EXISTE
                    
                nombre_visitante = equipos[1].string.strip().lower()
                link_visitante = equipos[1].parent['href']
                #CREAMOS EL EQUIPO SI NO EXISTE

                resultado_enlace = p.find("a",class_="resultado")
                if resultado_enlace != None:
                    goles=re.compile('(\d+).*(\d+)').search(resultado_enlace.string.replace('\n','').strip())
                    goles_l=int(goles.group(1))
                    goles_v=int(goles.group(2))
                    
                #CREAMOS EL PARTIDO 
              
    return True

def crearEquipo(nombre,link):
    try:
        f = urllib.request.urlopen("https://resultados.as.com" + link)
        s = BeautifulSoup(f,"lxml")
        
        info = s.find("section", class_="info-social")
        
        fundacion = info.find("strong", itemprop="foundingDate").string.strip()
        estadio = info.find(string=re.compile("Sede:")).parent.strong.string.strip()
        aforo = info.find(string=re.compile("Aforo:")).parent.strong.string.strip()
        if (info.find(string=re.compile("Dirección:"))):
            direccion = info.find(string=re.compile("Dirección:")).parent.strong.string.strip()
        else:
            direccion = "Desconocida"
        #CREAMOS EL EQUIPO       
    except:
        return False
    else:
        return True


