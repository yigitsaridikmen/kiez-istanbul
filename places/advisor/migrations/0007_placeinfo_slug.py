# Generated by Django 5.0.1 on 2024-02-04 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advisor', '0006_remove_placeinfo_activity_placeinfo_readable_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='placeinfo',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
