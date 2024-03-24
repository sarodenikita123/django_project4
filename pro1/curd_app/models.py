from django.db import models


class Registration(models.Model):
    ticket = [("VIP", "vip"), ("ST", "standard")]
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone_number = models.IntegerField()
    booking_date_time = models.DateField()
    ticket_type = models.CharField(max_length=20, choices=ticket)
    created_at = models.DateField(auto_now_add=True),
    updated_at = models.DateTimeField(auto_now=True)

