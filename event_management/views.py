from django.shortcuts import render
from django.db.models import Q
from app_event.models import Event, Category


# Homepage View:
def homepage(request):
    events = Event.objects.all()
    categories = Category.objects.all()
    query = request.POST.get('query', '')
    filter_cat = request.GET.get('category', '')

    # Search Functionality
    if query:
        events = events.filter(Q(name__icontains=query) | Q(location__icontains=query) | Q(date__icontains=query))

    if filter_cat:
        events = events.filter(category__name=filter_cat)

    context = {'events': events, 'categories': categories, 'selected_cat': filter_cat, 'title': 'Home'}
    return render(request, 'index.html', context)