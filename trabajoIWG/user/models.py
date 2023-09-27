from django.db import models

# Create your models here.

class userData(models.Model):
    userClass = models.PositiveIntegerField() #Distincion entre persona y entidad
    userType = models.CharField() #Rubro o rol de la persona
    userName = models.CharField(max_length=15, unique=True) #Nombre de usuario
    userPass = models.CharField #Contrasela del usuario
    realName = models.CharField() #Nombre real de la persona (opcional)
    userEmail = models.CharField(unique=True, primary_key=True) #Email del usuario
    userCountry = models.CharField() #Pais del usuario
    userFollwers = models.PositiveIntegerField() #Cantidad de segiudores
    userQualy = models.FloatField() #Calificacion que tendra el usuario (0 a 5)
    userDescr= models.CharField(max_length=150) #Descripcion del usuario *
    #puede quiza incluir foto?

    #esto por ahora no es funcional