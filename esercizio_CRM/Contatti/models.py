from django.db import models

from Clienti.models import cliente

# Create your models here.
class contatto(models.Model): 
    nome = models.CharField(max_length = 100)
    cognome = models.CharField(max_length = 100)
    ruolo = models.CharField(max_length = 100)
    cliente = models.ForeignKey(cliente, on_delete = models.CASCADE)

    def __str__(self):
        return self.nome + " " + self.cognome


class email(models.Model): 
    email = models.EmailField() 
    contatto = models.ForeignKey(contatto, on_delete = models.CASCADE)

    def __str__(self):
        return self.email


class telefono(models.Model): 
    telefono = models.CharField(max_length = 10)
    contatto = models.ForeignKey(contatto, on_delete = models.CASCADE)

    def __str__(self):
        return self.telefono

class interview(models.Model): 
    cliente =  models.ForeignKey(cliente, on_delete = models.CASCADE)
    contatto = models.ForeignKey(contatto, on_delete = models.CASCADE)
    interview = models.TextField(max_length = 1000)

    def __str__(self):
        return self.cliente.denominazione + " - " + self.contatto.nome + " " + self.contatto.cognome 


