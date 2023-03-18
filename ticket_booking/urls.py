from django.urls import path
from .views import index, event_details, book_ticket,event,send_email
app_name = 'admin'

urlpatterns = [
    path('', index, name='home'),
    path('event/', event, name='event'),
    path('event/<int:id>/', event_details, name='event_details'),
    path('event/<int:id>/book_ticket', book_ticket, name='book_ticket'),
    
    path('qr/',send_email,name='qr_code'),
    
]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()