from rest_framework import serializers
from . import models

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ('uuid', 'title', 'amazonurl', 'reating', 'description', 'author', 'printlength',
                  'language', 'price', 'isdiscount', 'discount', 'discount_price')

class CreateBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ('title', 'amazonurl', 'reating', 'description', 'author', 'printlength',
                  'language', 'price', 'isdiscount', 'discount', 'discount_price') 
        
class DelBookSerializer(serializers.ModelSerializer):    
    uuid = serializers.UUIDField()
    
    class Meta:
        model = models.Book
        fields = ('uuid',)