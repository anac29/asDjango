from django.db import models

# Create your models here.
class Equipo(models.Model):
    nombre = models.CharField(max_length=10,unique=True)
    ano_fundacion = models.IntegerField()
    estadio = models.CharField(max_length=30)
    aforo = models.IntegerField()
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.nombre)



class Temporada(models.Model):
    ano=models.IntegerField()

    def __str__(self):
        return '{}'.format(self.ano)
class Jornada(models.Model):
   numero=models.IntegerField()
   fecha=models.DateField()
   temporada=models.ForeignKey(Temporada,on_delete=models.CASCADE,related_name='Temporada')

   def __str__(self):
       return '{} by {}'.format(self.numero, self.temporada)



class Partido(models.Model):
    equipo_local=models.ForeignKey(Equipo,on_delete=models.CASCADE,related_name='Equipo_1')
    equipo_visitante= models.ForeignKey(Equipo,on_delete=models.CASCADE,related_name='Equipo_2')
    goles_local=models.IntegerField()
    goles_visitante=models.IntegerField()
    jornada=models.ForeignKey(Jornada,on_delete=models.CASCADE,related_name='Jornada')

    def __str__(self):
        return '{} by {}'.format(self.equipo_local, self.equipo_visitante)

