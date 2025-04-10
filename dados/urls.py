from django.urls import path
from . import views

urlpatterns = [
    path('', views.lanzar_dados, name='lanzar_dados'),
]

