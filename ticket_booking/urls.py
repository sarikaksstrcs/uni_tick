from django.urls import path
from .views import index, event_details, book_ticket,event_search
app_name = 'admin'

urlpatterns = [
    path('', index, name='home'),
    path('<int:id>/', event_details, name='event_details'),
    path('<int:id>/book_ticket', book_ticket, name='book_ticket'),
    path('event/search/', event_search, name='event_search'),
]