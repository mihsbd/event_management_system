from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=20, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=20, blank=True)
    mobile = models.CharField(max_length=14, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}'s Profile"