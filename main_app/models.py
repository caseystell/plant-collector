from django.db import models
from django.urls import reverse

class Plant(models.Model):
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    bears_fruit = models.BooleanField()
    flowers = models.BooleanField()

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'plant_id': self.id})