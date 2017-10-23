from rest_framework import generics
from django.views import generic
from .serializers import GrocerylistSerializer, GroceryitemSerializer
from .models import Grocerylist, Groceryitem

class CreateView_List(generics.ListCreateAPIView):
    queryset = Grocerylist.objects.all()
    serializer_class = GrocerylistSerializer

    def perform_create(self, serializer):
        serializer.save()

class DetailsView_List(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grocerylist.objects.all()
    serializer_class = GrocerylistSerializer

class CreateView_Item(generics.ListCreateAPIView):
    queryset = Groceryitem.objects.all()
    serializer_class = GroceryitemSerializer

    def perform_create(self, serializer):
        serializer.save()

class DetailsView_Item(generics.RetrieveUpdateDestroyAPIView):
    queryset = Groceryitem.objects.all()
    serializer_class = GroceryitemSerializer

class DetailsViewByFk_Item(generics.ListAPIView):
    serializer_class = GroceryitemSerializer

    def get_queryset(self):
        print(self.kwargs)
        return Groceryitem.objects.filter(grocerylist=self.kwargs['grocerylist'])