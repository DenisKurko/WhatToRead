from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('profile', views.index),
    path('search', views.index),
    path('addbook', views.index)
]
