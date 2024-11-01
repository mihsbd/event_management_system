from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'


class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
    capacity = models.PositiveIntegerField(default=100)
    attendees = models.ManyToManyField(User, related_name="booked_events", blank=True)
    
    def __str__(self):
        return self.name
    
    @property
    def is_fully_booked(self):
        return self.attendees.count() >= self.capacity