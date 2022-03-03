from django.urls import path
from . import views

app_name = "shop"
urlpatterns = [
    path("", views.index, name="index"),
    path("/create", views.create),
    path("/<id>", views.single),
    path("/<id>/update", views.update),
    path("/<id>/buy", views.buy),
]