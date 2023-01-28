from django.db import models
from app.models import Commande, Responsable, Materiel, Typeoper


class Detailcommande(models.Model):
    Quantite = models.IntegerField()
    PrixUnit = models.IntegerField()
    NombreJour = models.IntegerField()
    commande = models.ForeignKey(Commande, on_delete = models.CASCADE)
    materiel = models.ForeignKey(Materiel, on_delete = models.CASCADE)
    responsable = models.ForeignKey(Responsable, on_delete = models.CASCADE)
    typeoper = models.ForeignKey(Typeoper, on_delete = models.CASCADE)

    

