# Generated by Django 5.0.1 on 2024-01-22 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('county', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('place_type', models.CharField(choices=[('Bar', 'Bar'), ('Club', 'Club'), ('Cafe', 'Cafe'), ('Food', 'Food')], max_length=10)),
                ('activity', models.CharField(max_length=50)),
                ('largegroup', models.BooleanField()),
                ('alone', models.BooleanField()),
                ('dateable', models.BooleanField()),
                ('price_category', models.CharField(choices=[('Cheap', 'Cheap'), ('Normal', 'Normal'), ('Expensive', 'Expensive')], default='Normal', max_length=10)),
                ('kitchen', models.BooleanField()),
                ('smoke', models.BooleanField()),
                ('door_policy', models.BooleanField()),
                ('loudness', models.CharField(choices=[('Silent', 'Silent'), ('Moderate', 'Moderate'), ('Loud', 'Loud')], default='Moderate', max_length=10)),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField()),
            ],
        ),
    ]