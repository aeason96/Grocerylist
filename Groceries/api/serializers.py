from rest_framework import serializers
from .models import Grocerylist, Groceryitem

class GrocerylistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grocerylist
        fields = ('id', 'name')

class GroceryitemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Groceryitem
        fields = ('id', 'name', 'grocerylist')