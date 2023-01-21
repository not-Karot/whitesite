from django.db import models
from enum import Enum
class Color(Enum):
    A1 ="A1"
    A2 ="A2"
    A3 ="A3"
    A3_5 = "A3,5"
    A4 ="A4"
    B1 ="B1"
    B2 ="B2"
    B3 ="B3"
    B4 ="B4"
    C1 ="C1"
    C2 ="C2"
    C3 ="C3"
    C4 ="C4"
    D2 ="D2"
    D3 ="D3"
    D4 ="D4"


# Create your models here.
class Dentist(models.Model):
    dentist_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=60)

    def __str__(self):
        return self.username

    def get_clients(self):
        return self.client_set.all()
class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=50)
    dentist = models.ForeignKey(
        Dentist,
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='clients/', default='./../user-icon.png')
    def __str__(self):
        return self.name + self.surname


class TeethColor(models.Model):
    teethcolor_id = models.AutoField(primary_key=True)
    color = models.CharField(max_length=4, choices=[(tag.name, tag.value) for tag in Color])
    date = models.DateField()
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.color + str(self.date) + self.client.name
