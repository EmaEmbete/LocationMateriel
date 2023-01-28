from django.db import models



class Agence(models.Model):
    NomAgence = models.CharField(max_length=45)
    Nature = models.CharField(max_length=20)
    Nif = models.IntegerField()
    RegistreCom = models.CharField(max_length=60)
    AdressePhysique = models.CharField(max_length=70)
    Email = models.EmailField(max_length=20)
    telephone = models.CharField(max_length=13)

    def __str__(self):
        return self.NomAgence