from django.urls import path
from . import views

app_name = "shop"
urlpatterns = [
    path("", views.index, name="index"),
    path("/create", views.create, name="create"),
    path("/<id>", views.index, name="single"),
    path("/<id>/update", views.update, name="single"),
]