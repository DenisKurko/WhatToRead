from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
import uuid

# Create your models here.
class Book(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(default='', max_length=128)
    amazonurl = models.CharField(unique=True, null=False, max_length=1024)
    reating = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    description = models.TextField()
    author = models.CharField(max_length=64)
    printlength = models.IntegerField()
    language = models.CharField(max_length=64)
    price = models.IntegerField()
    isdiscount = models.BooleanField(default=False)
    discount = models.IntegerField(default='0')
    discount_price = models.IntegerField()