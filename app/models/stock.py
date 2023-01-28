from django.db import models
from app.models import Materiel, Typeoper



class Stock(models.Model):
    Quantitebrute = models.IntegerField()
    Quantiteloue = models.IntegerField()
    Quantitestock = models.IntegerField()
    Dateoperation = models.DateField()
    materiel = models.ForeignKey(Materiel, on_delete = models.CASCADE)
    typeoper = models.ForeignKey(Typeoper, on_delete = models.CASCADE)