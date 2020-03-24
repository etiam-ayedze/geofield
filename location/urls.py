from django.urls import path
from . import views

urlpatterns = [
    # path('', views.location_page, name='location_page'),
    # path('region/', views.region_page, name='region_page'),
    path('', views.save_region, name='save_region'),

]