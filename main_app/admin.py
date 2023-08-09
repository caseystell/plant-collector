from django.contrib import admin
from .models import Plant, Watering, Material

admin.site.register(Plant)
admin.site.register(Watering)
admin.site.register(Material)