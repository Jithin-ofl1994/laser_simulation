from django.urls import path
from laser_simulation_project import views

urlpatterns = [
    path("", views.home, name="home"),
    path("simulation", views.simulation, name="simulation"),
]