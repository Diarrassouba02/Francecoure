from django.urls import path
from . import views

urlpatterns = [
path('',views.archive, name = 'archive'),
path('pronostics',views.pronostics, name = 'pronostics'),
path('abonnement',views.abonnement, name = 'abonnement'),
path('acceuil',views.acceuil, name = 'acceuil'),
path('contact',views.contact, name = 'contact'),


]