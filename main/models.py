from django.db import models


class Bimbo(models.Model):
    nome = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50, unique=True)
    email = models.EmailField(blank=True)
    aggiunto = models.DateTimeField(auto_now_add=True)
    num_incontri = models.IntegerField(default=0)

    def __str__(self):
        return str(self.nome)
