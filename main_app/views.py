from django.shortcuts import render

plants = [
    {'name': 'Prickly Pear', 'type': 'Cactus', 'description': 'Paddle-shaped leaves grow in a cluster formation. Caution: very spiky!', 'bears_fruit': True, 'flowers': True},
    {'name': 'Desert Willow', 'type': 'Tree', 'description': 'Long thin green leaves and a wide-spread shape', 'bears_fruit': False, 'flowers': True},
    {'name': 'Ice Plant', 'type': 'Succulent', 'description': 'Finger-shaped leaves; makes for an excellent ground cover and requires little water', 'bears_fruit': False, 'flowers': True},
    {'name': 'Ocotillo', 'type': 'Cactus', 'description': 'Long spiky arms reach up toward the sky; grows beautiful green leaves with lots of rain!', 'bears_fruit': False, 'flowers': True},
    {'name': 'Peach Tree', 'type': 'Tree', 'description': 'Brown bark with banana-shaped leaves; grows fairly tall', 'bears_fruit': True, 'flowers': True},
]

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def plants_index(request):
  return render(request, 'plants/index.html', {
    'plants': plants,
  })