from django.contrib import admin

# Register your models here.
from whiteapi.models import Dentist, Client, TeethColor

admin.site.register(Dentist)
admin.site.register(Client)
admin.site.register(TeethColor)