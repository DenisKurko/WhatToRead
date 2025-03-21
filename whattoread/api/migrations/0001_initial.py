# Generated by Django 5.1.6 on 2025-03-14 18:44

import django.core.validators
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(default=uuid.uuid4, editable=False)),
                ('title', models.CharField(default='', max_length=128)),
                ('amazonurl', models.CharField(max_length=1024, unique=True)),
                ('reating', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=64)),
                ('printlength', models.IntegerField()),
                ('language', models.CharField(max_length=64)),
                ('price', models.IntegerField()),
                ('isdiscount', models.BooleanField(default=False)),
                ('discount', models.IntegerField(default='0')),
                ('discount_price', models.IntegerField()),
            ],
        ),
    ]
