from django.db import models


sexe = (('Homme','Homme'), ('Femme', 'Femme'))

class Responsable(models.Model):
    NomRespo = models.CharField(max_length = 25)
    PrenomRespo = models.CharField(max_length = 20)
    Genre = models.CharField(choices = sexe, max_length = 10)
    DateNaiss = models.DateField()


    def __str__(self):
        return self.NomRespo+" "+self.PrenomRespo

