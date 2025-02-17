from django.db import models

# Create your models here.
class Book(models.Model):
    amazonurl = models.CharField(unique=True, null=False, max_length=1024)
    reating = models.IntegerField()
    description = models.TextField()
    author = models.CharField(max_length=64)
    printlength = models.IntegerField()
    language = models.CharField(max_length=64)
    price = models.IntegerField()
    isdiscount = models.BooleanField(default=False)
    discount = models.IntegerField(default='0')
    discount_price = models.IntegerField()
    skiped = models.BooleanField(default=False)
    liked = models.BooleanField(default=False)