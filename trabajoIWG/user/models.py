from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class userProfile(models.Model):
    userClass = models.PositiveIntegerField() #Distincion entre persona y entidad
    userPic = models.TextField()
    userType = models.CharField() #Rubro o rol de la persona profesion
    userCountry = models.CharField() #Pais del usuario
    userFollwers = models.PositiveIntegerField(null=True, default=0) #Cantidad de segiudores
    userQualy = models.FloatField(null=True, default=0.0) #Calificacion que tendra el usuario (0 a 5)
    userBio= models.CharField(max_length=150) #Descripcion del usuario *
    user = models.OneToOneField(User,on_delete=models.CASCADE, unique=True) #clase asociada a un usuario

class Posts(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) #clase asociada a un usuario
    nTitle = models.TextField() #Titulo de la noticia
    nBody = models.TextField() #El cuerpo de la noticia
    nImage = models.TextField() #Imagen
    lat = models.IntegerField(null=True, default = 0) #Posicion en el mapa lat
    lng = models.IntegerField(null=True, default = 0) #lng