# Generated by Django 5.0.1 on 2024-01-22 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advisor', '0002_alter_placeinfo_address_alter_placeinfo_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeinfo',
            name='city',
            field=models.CharField(default='Istanbul', max_length=100),
        ),
    ]