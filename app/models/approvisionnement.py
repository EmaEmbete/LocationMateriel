from django.db import models
from app.models import Fournisseur


class Approvisionnement(models.Model):
    Codeappro = models.IntegerField()
    Dateappro = models.DateField()
    fournisseur = models.ForeignKey(Fournisseur, on_delete = models.CASCADE)

    def __int__(self):
        return self.Codeappro

