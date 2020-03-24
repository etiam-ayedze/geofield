from django.urls import path
from . import views

urlpatterns = [
    path('proprietaire/', views.voir_proprio, name='voir_proprio'),
    path('landsinfos/proprio', views.save_proprio, name='proprio'),
    path('proprietaire/update/<int:id>', views.modifier_proprio, name='modify_proprio'),
    path('proprietaire/<int:id>/', views.delete_proprio, name='delete_proprio'),
    path('possession/<int:id>', views.liste_propriete, name='liste_propriete'),

    path('typeparcelle/', views.save_typeparcelle, name='type_parcelle'),
    path('typeparcelle/update/<int:id>', views.modifier_typeparcelle, name='modify_typeparcelle'),
    path('typeparcelle/<int:id>/', views.delete_typeparcelle, name='delete_typeparcelle'),

    path('typesuccession/', views.save_typesuccession, name='type_succession'),
    path('typesuccession/update/<int:id>', views.modifier_typesuccession, name='modify_typesuccession'),
    path('typesuccession/<int:id>', views.delete_typesuccession, name='delete_typesuccesion'),

    path('parcelle/', views.save_parcelle, name='parcelle'),
    path('landsinfos/', views.save_lands_info, name='landsinfos'),
    path('landsdetails/<int:id>', views.detailParcelle, name='landdetail'),
    path('landsdetails/vue/<int:id>/', views.parcelleDetailvue, name='parcelleDetailsVue'),


    path('stat1/', views.statFile1, name='stat1'),
    path('statisticMonth/', views.parcelleParMois, name='parcelleParMois'),


]












































