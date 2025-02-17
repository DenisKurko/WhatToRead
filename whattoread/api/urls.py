from django.urls import path
from .views import *

urlpatterns = [
    path('getbooks', BookView.as_view()),
]
