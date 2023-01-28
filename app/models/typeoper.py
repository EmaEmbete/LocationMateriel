from django.db import models


class Typeoper(models.Model):
    NomTypeoper = models.CharField(max_length = 25)


    def __str__(self):
        return self.NomTypeoper

    