from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('ticket_booking.urls', namespace='ticket_booking')),
    path('admin/', admin.site.urls),
    path('ticket_admin/', include('ticket_admin.urls', namespace='ticket_admin')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
