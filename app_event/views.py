from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Category, Event
from .forms import CategoryForm, EventForm


# Create Category View:
@login_required
def category(request):
    if request.user.is_superuser:
        categories = Category.objects.all()

        if request.method == 'POST':
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Category Created Successfully!")
                return redirect('category')
        else:
            form = CategoryForm()

        context = {'categories': categories, 'form': form, 'title': 'Category'}
        return render(request, 'app_event/categories.html', context)
    else:
        return redirect('home')


# Remove Category View:
@login_required
def remove_category(request, cat_id):
    if not request.user.is_superuser:
        return redirect('home')
    
    category = Category.objects.get(id=cat_id)
    category.delete()
    messages.success(request, "Category Deleted Successfully!")
    return redirect('category')


# Event Create View:
@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            messages.success(request, "Event Created Successfully!")
            return redirect('event_list')
    else:
        form = EventForm()
    
    context = {'form': form, 'title': 'Create Event', 'color': 'success'}
    return render(request, 'app_event/event_form.html', context)


# Event Update View:
@login_required
def update_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if event.created_by != request.user and not request.user.is_superuser:
        return redirect('event_detail', event_id=event.id)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, "Event Updated Successfully!")
            return redirect('event_detail', event_id=event.id)
    else:
        form = EventForm(instance=event)

    context = {'form': form, 'title': 'Update Event', 'color': 'warning'}
    return render(request, 'app_event/event_form.html', context)


# Event List View:
@login_required
def event_list(request):
    events = Event.objects.filter(created_by=request.user)
    context = { 'events': events, 'title': 'Event List' }
    return render(request, 'app_event/event_list.html', context)


# Event Detail View:
def event_detail(request, event_id):
    user = request.user
    event = get_object_or_404(Event, id=event_id)
    is_booked = user in event.attendees.all() if user.is_authenticated else False
    context = { 'event': event, 'is_booked': is_booked, 'title': 'Event Detail' }
    return render(request, 'app_event/event_detail.html', context)


# Event Delete View:
@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if event.created_by != request.user and not request.user.is_superuser:
        return redirect('event_detail', event_id=event.id)

    if request.method == 'POST':
        event.delete()
        messages.success(request, "Event Deleted Successfully!")
        return redirect('event_list')
    
    context = {'event': event, 'title': 'Confirm Delete'}
    return render(request, 'app_event/event_delete.html', context)