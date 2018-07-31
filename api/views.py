# Your imports should be here
from rest_framework.generics import ListAPIView, DestroyAPIView, RetrieveUpdateAPIView, RetrieveAPIView
from restaurants.models import Restaurant
from .serializers import RestaurantListSerializer, DetailRestaurantSerializer


# Complete me! I should be your APIListView
class RestaurantListView(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer


class DetailView(RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = DetailRestaurantSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'rest_id'


class UpdateListView(RetrieveUpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'rest_id'


class DeleteListView(DestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'rest_id'