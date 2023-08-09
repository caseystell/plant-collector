from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Plant, Material
from .forms import WateringForm

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def plants_index(request):
  plants = Plant.objects.all()
  return render(request, 'plants/index.html', {
    'plants': plants,
  })

def plants_detail(request, plant_id):
  plant = Plant.objects.get(id=plant_id)
  id_list = plant.materials.all().values_list('id')
  materials_plant_doesnt_have = Material.objects.exclude(id__in=id_list)
  watering_form = WateringForm()
  return render(request, 'plants/detail.html', { 
    'plant': plant,
    'watering_form': watering_form,
    'materials': materials_plant_doesnt_have
    })

def add_watering(request, plant_id):
  form = WateringForm(request.POST)
  if form.is_valid():
    new_watering = form.save(commit=False)
    new_watering.plant_id = plant_id
    new_watering.save()
  return redirect('detail', plant_id=plant_id)

class PlantCreate(CreateView):
  model = Plant
  fields = '__all__'

class PlantUpdate(UpdateView):
  model = Plant
  fields = ['type', 'description', 'bears_fruit', 'flowers']

class PlantDelete(DeleteView):
  model = Plant
  success_url = '/plants'

class MaterialList(ListView):
  model = Material

class MaterialDetail(DetailView):
  model = Material

class MaterialCreate(CreateView):
  model = Material
  fields = '__all__'

class MaterialUpdate(UpdateView):
  model = Material
  fields = ['name', 'made_of']

class MaterialDelete(DeleteView):
  model = Material
  success_url = '/materials'

def assoc_material(request, plant_id, material_id):
  Plant.objects.get(id=plant_id).materials.add(material_id)
  return redirect('detail', plant_id=plant_id)

def disassoc_material(request, plant_id, material_id):
  Plant.objects.get(id=plant_id).materials.remove(material_id)
  return redirect('detail', plant_id=plant_id)