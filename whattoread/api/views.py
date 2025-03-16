from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from . import models, serializers


class BookView(generics.ListAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    
class AddBookView(APIView):
    serializer_class = serializers.CreateBookSerializer
    
    def post(self, request, format=None):    
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():  
            title = serializer.data["title"]
            amazonurl = serializer.data["amazonurl"]
            reating = serializer.data["reating"]
            description = serializer.data["description"]
            author = serializer.data["author"]
            printlength = serializer.data["printlength"]
            language = serializer.data["language"]
            price = serializer.data["price"]
            isdiscount = serializer.data["isdiscount"]
            discount = serializer.data["discount"]
            discount_price = serializer.data["discount_price"]
            
            queryset = models.Book.objects.filter(title=title)
            
            if queryset.exists():
                book = queryset[0]
                return Response([{'message': 'Book already exists'}, serializers.BookSerializer(book).data], 
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                book = models.Book(title=title,
                                   amazonurl=amazonurl,
                                   reating=reating, 
                                   description=description,
                                   author=author,
                                   printlength=printlength,
                                   language=language,
                                   price=price,
                                   isdiscount=isdiscount,
                                   discount=discount,
                                   discount_price=discount_price)
                book.save()
                return Response([{'message': 'Book Added'}, serializers.BookSerializer(book).data], 
                                status=status.HTTP_201_CREATED)
        else:
            return Response([{'message': 'Invalid Data'}, serializer.errors], 
                            status=status.HTTP_400_BAD_REQUEST)

class DelBookView(APIView):
    serializer_class = serializers.DelBookSerializer
    
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            uuid = serializer.validated_data["uuid"]
            
            queryset = models.Book.objects.filter(uuid=uuid)
            
            if queryset.exists():
                book = queryset[0]
                book.delete()
                
                return Response([{'message': 'Book Deleted'}, serializers.BookSerializer(book).data],
                                status=status.HTTP_200_OK)
            else:
                return Response([{'message': 'Book Not Found'}],
                                status=status.HTTP_404_NOT_FOUND)
        else:
            return Response([{'message': 'Invalid Data'}, serializer.errors], 
                            status=status.HTTP_400_BAD_REQUEST)