from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class PlaceInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100,default='Istanbul')
    county = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    TYPE_CHOICES = [
        ('Bar', 'Bar'),
        ('Club', 'Club'),
        ('Cafe', 'Cafe'),
        ('Food', 'Food'),
    ]    
    place_type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES, # You can set a default value if needed
    )

    #activity = models.CharField(max_length=50)
    
    largegroup = models.BooleanField()
    alone = models.BooleanField()
    dateable = models.BooleanField()

    PRICE_CHOICES = [
        ('Cheap', 'Cheap'),
        ('Normal', 'Normal'),
        ('Expensive', 'Expensive'),
    ]

    price_category = models.CharField(
        max_length=10,
        choices=PRICE_CHOICES,
        default='Normal',  # You can set a default value if needed
    )
    kitchen = models.BooleanField()
    smoke = models.BooleanField()
    door_policy = models.BooleanField()
    readable = models.BooleanField(default=False)
    workable = models.BooleanField(default=False)
    LOUDNESS_CHOICES = [
        ('Silent', 'Silent'),
        ('Moderate', 'Moderate'),
        ('Loud', 'Loud'),
    ]    
    loudness = models.CharField(
        max_length=10,
        choices=LOUDNESS_CHOICES,
        default='Moderate',  # You can set a default value if needed
    )
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
