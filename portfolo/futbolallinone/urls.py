from django.urls import path
from . import views


urlpatterns = [
    path("", views.futbol_index, name="futbol_index"),
]
