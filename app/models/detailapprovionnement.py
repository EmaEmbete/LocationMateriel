from django.db import models
from app.models import Approvisionnement, Responsable, Materiel


class Detailapprovionnement(models.Model):
    Quantite = models.IntegerField()
    Prixunit = models.IntegerField()
    approvisionnement = models.ForeignKey(Approvisionnement, on_delete = models.CASCADE) 
    responsable = models.ForeignKey(Responsable, on_delete = models.CASCADE) 
    materiel = models.ForeignKey(Materiel, on_delete = models.CASCADE)