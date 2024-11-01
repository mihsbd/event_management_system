from django.contrib import admin
from .models import Category, Event

admin.site.register(Category)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'category', 'created_by')
    list_filter = ('category', 'date')
    search_fields = ('name', 'location')

    def is_fully_booked(self, obj):
        return obj.is_fully_booked
    is_fully_booked.boolean = True