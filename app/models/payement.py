from django.db import models
from app.models import Client, Commande, Responsable



class Payement(models.Model):
    Datepayement = models.DateField()
    Motif = models.CharField(max_length = 50)
    Bordereau = models.FileField()
    client = models.ForeignKey(Client, on_delete = models.CASCADE)
    commande = models.ForeignKey(Commande, on_delete = models.CASCADE)
    responsable = models.ForeignKey(Responsable, on_delete = models.CASCADE)
    Codepayement = models.IntegerField()
    etat = models.CharField(max_length = 50)


    def __int__(self):
        return self.Codepayement

