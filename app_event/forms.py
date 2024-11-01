from django import forms
from .models import Category, Event


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=25, required=True, label="Category Name")

    class Meta:
        model = Category
        fields = ['name']


class EventForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))
    class Meta:
        model = Event
        fields = ['name', 'date', 'location', 'description', 'category', 'capacity']
        widgets = { 'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}), }