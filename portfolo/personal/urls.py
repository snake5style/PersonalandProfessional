from django.urls import path
from . import views


urlpatterns = [
    path("", views.personal_index, name="personal_index"),
    path("about_index", views.about_index, name="about_index"),

]
