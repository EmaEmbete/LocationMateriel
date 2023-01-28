from django.db import models
from app.models import Categorie, Agence, Responsable


class Materiel(models.Model):
    NomMateriel = models.CharField(max_length = 40)
    categorie = models.ForeignKey(Categorie, on_delete = models.CASCADE)
    agence = models.ForeignKey(Agence, on_delete = models.CASCADE)
    responsable = models.ForeignKey(Responsable, on_delete = models.CASCADE)

    def __str__(self):

        return self.NomMateriel
