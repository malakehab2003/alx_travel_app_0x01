from django.shortcuts import render
from rest_framework import generics
from .models import Listing, Booking, Review
from .serializers import ListingSerializer, BookingSerializer, ReviewSerializer

class ListingListCreateView(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

    def perform_create(self, serializer):
        serializer.save(host=self.request.user)

class ReviewListCreateView(generics.ListCreateAPIView):
    queryet = Review.objects.all()
    serialzer_class = ReviewSerializer

class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

