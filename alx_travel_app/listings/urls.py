from django.urls import path
from .views import ListingListCreateView, BookingListCreateView, ReviewListCreateView

urlpatterns = [
    path('listings/', ListingListCreateView.as_view(), name='listing-list-create'),
    path('bookings/', BookingListCreateView.as_view(), name='booking-list-create'),
    path('review/', ReviewListCreateView.as_view(), name='review-list-create'),
]