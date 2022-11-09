from django.db import models



# Create your models here.
class cliente(models.Model): 
    denominazione = models.CharField(max_length = 100)
    indirizzo = models.CharField(max_length = 100)
    cap = models.CharField(max_length = 5)
    città = models.CharField(max_length = 100)
    provincia = models.CharField(max_length = 4)
    telefono = models.CharField(max_length = 15)
    email = models.CharField(max_length = 50)
    partita_iva = models.CharField(max_length = 11)
     
    def __str__(self): 
        return self.denominazione
