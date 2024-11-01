from django.urls import path
from . import views

urlpatterns = [
    path('<int:event_id>', views.book_event, name='book_event'),
    path('<int:event_id>/unbook', views.unbook_event, name='unbook_event'),
    path('list', views.booking_list, name='booking_list'),
]