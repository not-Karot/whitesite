from rest_framework import serializers

from .models import Dentist, Client, TeethColor


class DentistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dentist
        fields = ('dentist_id', 'username', 'email', 'password')


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ('client_id', 'name', 'surname', 'dentist', 'image')


class TeethColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeethColor
        fields = ('teethcolor_id', 'color', 'date', 'client')
