from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app_event.models import Event


# Book Event View:
@login_required
def book_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if event.created_by == request.user:
        messages.error(request, "This Event is Created By You.")
    elif request.user.is_superuser:
        messages.error(request, "Admin Accounts are Ineligible for Event Bookings.")
    elif event.is_fully_booked:
        messages.error(request, "This Event is Fully Booked.")
    elif request.user in event.attendees.all():
        messages.info(request, "You have Already Booked this Event.")
    else:
        event.attendees.add(request.user)
        messages.success(request, "Event Booked Successfully!")
    
    return redirect('event_detail', event_id=event.id)


# Unbook Event View:
@login_required
def unbook_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.user in event.attendees.all():
        event.attendees.remove(request.user)
        messages.warning(request, "Booking Canceled Successfully.")
    else:
        messages.info(request, "You do not have a Booking for this Event.")
    
    return redirect('event_detail', event_id=event.id)


# Booked Events View:
@login_required
def booking_list(request):
    events = request.user.booked_events.all()
    context = {'events': events, 'title': 'Booked Events'}
    return render(request, 'app_book/booking_list.html', context)