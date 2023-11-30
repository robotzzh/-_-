from django.urls import path
from . import views

urlpatterns = [
    path("/insert", views.insert_student, name='/insert'),
    path("/select", views.select_student, name='/select'),
    path("/delete", views.delete_student, name='/delete'),
    path("/alert", views.alert_student, name='/alert'),
    path("", views.menu, name="menu"),
]