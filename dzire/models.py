from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):

    car_brand=models.CharField(max_length=20)
    car_model=models.CharField(max_length=20)
    car_variant=models.CharField(max_length=20)
    fuel=models.CharField(max_length=20)
    owner_name=models.CharField(max_length=20)
    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date=timezone.now()
        delf.save()

    def __str__(self):
        return self.owner_name
