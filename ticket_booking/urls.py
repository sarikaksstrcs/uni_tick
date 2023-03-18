from django.urls import path
<<<<<<< HEAD
from .views import index, event_details, book_ticket,event_search
=======
from .views import index, event_details, book_ticket
>>>>>>> 0736a3469168106510384aeaee29a82c3e945d51
app_name = 'admin'

urlpatterns = [
    path('', index, name='home'),
    path('<int:id>/', event_details, name='event_details'),
    path('<int:id>/book_ticket', book_ticket, name='book_ticket'),
<<<<<<< HEAD
    path('event/search/', event_search, name='event_search'),
=======
>>>>>>> 0736a3469168106510384aeaee29a82c3e945d51
]