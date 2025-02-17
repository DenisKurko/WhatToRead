from rest_framework import serializers
from .models import *

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'amazonurl', 'reating', 'description', 'author', 'printlength',
                  'language', 'price', 'isdiscount', 'discount', 'discount_price')