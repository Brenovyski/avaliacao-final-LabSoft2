from django.db import models

class Ticket(models.Model):
    seat_number = models.CharField(max_length=10, unique=True)
