from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import viewsets

from .serializers import DentistSerializer, ClientSerializer, TeethColorSerializer
from .models import Dentist, Client, TeethColor


class DentistViewSet(viewsets.ModelViewSet):
    queryset = Dentist.objects.all().order_by('dentist_id')
    serializer_class = DentistSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all().order_by('dentist')
    serializer_class = ClientSerializer


class TeethColorViewSet(viewsets.ModelViewSet):
    queryset = TeethColor.objects.all().order_by('teethcolor_id')
    serializer_class = TeethColorSerializer
