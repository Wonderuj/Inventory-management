from django.shortcuts import render

# Create your views here.
from .models import inventory
from .serializers import inventorySerializer

from rest_framework import viewsets

class inventoryView(viewsets.ModelViewSet):
    queryset=inventory.objects.all()
    serializer_class=inventorySerializer

