from django.db import models
from app.models import Responsable



class Client(models.Model):
    NomClient = models.CharField(max_length = 50)
    Adresse = models.CharField(max_length = 60)
    Telephone = models.CharField(max_length = 13)
    Email = models.EmailField(max_length = 60)
    responsable = models.ForeignKey(Responsable, on_delete = models.CASCADE)


    def __str__(self):
        return self.NomClient +" Tel: "+self.Telephone