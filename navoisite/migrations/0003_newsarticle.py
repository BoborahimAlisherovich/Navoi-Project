# Generated by Django 5.0.6 on 2024-06-01 05:34

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navoisite', '0002_contact_subjact'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=100)),
                ('main_image', models.ImageField(upload_to='Articles/photo')),
            ],
        ),
    ]
