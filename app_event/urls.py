from django.urls import path
from . import views

urlpatterns = [
    path('category', views.category, name='category'),
    path('category/remove/<int:cat_id>', views.remove_category, name='remove_category'),
    path('create', views.create_event, name='create_event'),
    path('list', views.event_list, name='event_list'),
    path('detail/<int:event_id>', views.event_detail, name='event_detail'),
    path('update/<int:event_id>', views.update_event, name='update_event'),
    path('delete/<int:event_id>', views.delete_event, name='delete_event'),
]
