from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('readings/', views.readings, name='readings'),
    path('symptoms/', views.symptoms, name='symptoms'),
    path('influences/', views.influences, name='influences'),
    path('methods/', views.methods, name='methods'),
    path('system/', views.system, name='system'),
    path('tips/', views.tips, name='tips'),
]