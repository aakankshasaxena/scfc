from django.db import models

class School(models.Model):
    name = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    emissions = models.FloatField()
 
    def __str__(self):
        return self.name