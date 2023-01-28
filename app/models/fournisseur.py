from django.db import models


class Fournisseur(models.Model):
    NomFournisseur = models.CharField(max_length = 35)
    Adresse = models.CharField(max_length = 35)
    Telephone = models.CharField(max_length = 13)
    Email = models.EmailField(max_length = 35)


    def __str__(self):
        return self.NomFournisseur