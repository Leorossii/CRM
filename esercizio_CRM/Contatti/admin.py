from calendar import c
from django.contrib import admin

# Register your models here.
from .models import contatto,email,telefono,interview

    



admin.site.register(contatto)
admin.site.register(email)
admin.site.register(telefono)
admin.site.register(interview)