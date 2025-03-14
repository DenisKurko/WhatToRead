from django.urls import path
from . import views

urlpatterns = [
    path('getbooks', views.BookView.as_view()),
    path('addbook', views.AddBookView.as_view())
]
