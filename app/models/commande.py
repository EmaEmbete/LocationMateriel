from django.db import models
from app.models import Client


class Commande(models.Model):
    CodeCommande = models.IntegerField()
    DateCommande = models.DateField()
    client = models.ForeignKey(Client, on_delete = models.CASCADE)


    def __int__(self):
        self.CodeCommande
