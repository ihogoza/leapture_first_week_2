from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('display/', views.home_view, name='home'),
    
]