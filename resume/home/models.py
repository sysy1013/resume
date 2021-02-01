from django.db import models
from django.conf import settings

class Resume(model.Model):
    name = models.CharField(max_legth=20)
    
    description = models.TextField()
    techhnologh = models.TextField()
    goal = models.charField(max_leght=100)

