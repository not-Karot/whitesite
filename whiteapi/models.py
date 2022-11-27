from django.db import models


# Create your models here.
class Dentist(models.Model):
    dentist_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=60)

    def __str__(self):
        return self.username


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=50)
    dentist = models.ForeignKey(
        Dentist,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name + self.surname


class TeethColor(models.Model):
    teethcolor_id = models.AutoField(primary_key=True)
    color = models.CharField(max_length=4)
    date = models.DateField()
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.color + str(self.date) + self.client.name
