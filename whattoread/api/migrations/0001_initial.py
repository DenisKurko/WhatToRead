# Generated by Django 5.1.6 on 2025-02-17 19:52

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
                ('whattoreadarticle', models.IntegerField(unique=True)),
                ('amazonurl', models.CharField(max_length=1024, unique=True)),
                ('reating', models.IntegerField()),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=64)),
                ('printlength', models.IntegerField()),
                ('language', models.CharField(max_length=64)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField(default='0')),
                ('isdiscount', models.BooleanField(default=False)),
                ('discount_price', models.IntegerField()),
                ('skiped', models.BooleanField(default=False)),
                ('liked', models.BooleanField(default=False)),
            ],
        ),
    ]
