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
    def get_queryset(self):
        dentist_id = self.request.query_params.get('dentist_id', None)
        if dentist_id is not None:
            dentist = Dentist.objects.get(dentist_id=dentist_id)
            queryset = Client.objects.filter(dentist=dentist)
        else:
            queryset = Client.objects.all()
        return queryset.order_by('dentist')


class TeethColorViewSet(viewsets.ModelViewSet):
    queryset = TeethColor.objects.all().order_by('teethcolor_id')
    serializer_class = TeethColorSerializer
