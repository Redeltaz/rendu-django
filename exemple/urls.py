from django.urls import path
from . import views

app_name ='app_python'
urlpatterns = [
    path('', views.index),
    path('/create', views.create),
    path('/<id>', views.details ),
    path('/<id>/update', views.update ),
    path('/<id>/delete', views.delete ),
]