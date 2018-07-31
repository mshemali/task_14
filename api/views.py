# Your imports should be here
from rest_framework.generics import ListAPIView, DestroyAPIView, RetrieveUpdateAPIView, RetrieveAPIView, CreateAPIView
from restaurants.models import Restaurant
from .serializers import RestaurantListSerializer, DetailRestaurantSerializer, CreateSerializer


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


class CreateView(CreateAPIView):
    serializer_class = CreateSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)