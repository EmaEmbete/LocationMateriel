from django.db import models



class Categorie(models.Model):
    NomCategorie = models.CharField(max_length = 25)


    def __str__(self):
        return self.NomCategorie
