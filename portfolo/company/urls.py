from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('pro_form', views.pro_form, name="pro_form"),
    path('list_details', views.list_details, name="list_details"),
    path('edit_form/<int:id>/', views.edit_form, name="edit_form"),
    path('update_form/<int:id>', views.update_form, name="update_form"),
    path('delete_form/<int:id>', views.delete_form, name="delete_form"),


]
