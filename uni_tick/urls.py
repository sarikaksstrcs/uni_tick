from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('ticket_booking.urls', namespace='ticket_booking')),
    path('admin/', admin.site.urls),
    path('ticket_admin/', include('ticket_admin.urls', namespace='ticket_admin')),
]
