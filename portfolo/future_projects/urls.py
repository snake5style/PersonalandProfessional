from django.urls import path
from . import views


urlpatterns = [
    path("", views.future_index, name="future_index"),
    path("<int:pk>/", views.future_detail, name="future_detail"),
]
