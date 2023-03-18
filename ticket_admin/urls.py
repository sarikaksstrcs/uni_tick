from .views import index, events, create_event, delete_event, update_event, event_details, create_ticket_tier ,update_ticket_tier,delete_ticket_tier,create_parking_tier
from .views import tourist_spots
from django.urls import path

app_name = 'admin'

urlpatterns = [
    path('', index, name='home'),

    #for Events
    path('events/', events, name='events'),
    path('events/create/', create_event, name='create_event'),
    path('events/<int:id>/', event_details, name='event_details'),
    path('events/<int:id>/create_ticket_tier/',create_ticket_tier, name='create_ticket_tier'),
    path('events/<int:id>/update_ticket_tier/',
         update_ticket_tier, name='update_ticket_tier'),
    path('events/<int:id>/delete_ticket_tier/',
         delete_ticket_tier, name='delete_ticket_tier'),
     path('events/<int:id>/create_parking_tier/',
         create_parking_tier, name='create_parking_tier'),
    path('events/<int:id>/update/', update_event, name='update_event'),
    path('events/<int:id>/delete/', delete_event, name='delete_event'),

     #for Tourist Spots
    path('tourist_spots/', tourist_spots, name='tourist_spots'),
    path('tourist_spots/create/', tourist_spots, name='create_tourist_spots'),

    #for Amenities
    #path('amenities/create', create_amenities, name='create_amenities'),

]
