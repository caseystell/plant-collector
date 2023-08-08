from django.db import models
from django.urls import reverse
from datetime import date

TIMES = (
    ('M', 'Morning'),
    ('E', 'Evening')
)

FRUITS = (
    ('Y', 'Yes'),
    ('N', 'No')
)

FLOWERS = (
    ('Y', 'Yes'),
    ('N', 'No')
)

class Plant(models.Model):
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    bears_fruit = models.CharField(max_length=1, choices=FRUITS, default=FRUITS[1][0])
    flowers = models.CharField(max_length=1, choices=FLOWERS, default=FLOWERS[1][0])

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'plant_id': self.id})
    
    def watered_for_today(self):
        return self.watering_set.filter(date=date.today()).count() >= len(TIMES)
    
class Watering(models.Model):
    date = models.DateField('watering date')
    time = models.CharField(max_length=1, choices=TIMES, default=TIMES[0][0])
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_time_display()} on {self.date}'
    
    class Meta:
        ordering = ['-date']