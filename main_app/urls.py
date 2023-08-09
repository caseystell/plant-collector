from django.urls import path
from . import views
	
urlpatterns = [
	path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('plants/', views.plants_index, name='index'),
    path('plants/<int:plant_id>/', views.plants_detail, name='detail'),
    path('plants/create/', views.PlantCreate.as_view(), name='plants_create'),
    path('plants/<int:pk>/update/', views.PlantUpdate.as_view(), name='plants_update'),
    path('plants/<int:pk>/delete/', views.PlantDelete.as_view(), name='plants_delete'),
    path('plants/<int:plant_id>/add_watering/', views.add_watering, name='add_watering'),
    path('plants/<int:plant_id>/assoc_material/<int:material_id>/', views.assoc_material, name='assoc_material'),
    path('plants/<int:plant_id>/disassoc_material/<int:material_id>/', views.disassoc_material, name='disassoc_material'),
    path('materials/', views.MaterialList.as_view(), name='materials_index'),
    path('materials/<int:pk>/', views.MaterialDetail.as_view(), name='materials_detail'),
    path('materials/create/', views.MaterialCreate.as_view(), name='materials_create'),
    path('materials/<int:pk>/update/', views.MaterialUpdate.as_view(), name='materials_update'),
    path('materials/<int:pk>/delete/', views.MaterialDelete.as_view(), name='materials_delete'),
]