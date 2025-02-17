from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.
class BookView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer