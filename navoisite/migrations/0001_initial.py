# Generated by Django 5.0.6 on 2024-06-04 10:27

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('description', models.TextField()),
                ('subjact', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Elon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='Elons/photo')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=100)),
                ('main_image', models.ImageField(upload_to='Articles/photo')),
            ],
        ),
    ]
