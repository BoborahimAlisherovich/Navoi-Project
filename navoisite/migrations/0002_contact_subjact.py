# Generated by Django 5.0.6 on 2024-06-01 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navoisite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='subjact',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]