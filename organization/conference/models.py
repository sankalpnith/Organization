from django.db import models
from core.models import BaseModel


class ConferenceRoom(BaseModel):

    STATUS_AVAILABLE = 'AVAILABLE'
    STATUS_BOOKED = 'BOOKED'
    STATUS_CHOICES = (
        (STATUS_BOOKED, 'Booked'),
        (STATUS_AVAILABLE, 'Available'),
    )

    room_id = models.CharField(unique=True, max_length=20)
    booking_email = models.EmailField()
    name = models.CharField(max_length=100)
    sitting_count = models.IntegerField()
    status = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES,
        default=STATUS_AVAILABLE
    )
