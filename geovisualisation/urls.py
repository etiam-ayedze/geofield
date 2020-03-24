from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.visualize, name='visualize'),
    path('geovisualisation/', views.ParcelleVue.as_view(), name='parcelleVue'),
]