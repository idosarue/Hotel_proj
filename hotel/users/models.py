from django.db import models
from accounts.models import Profile


# Create your models here.
class Booking(models.Model):
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    room = models.ForeignKey('Room', on_delete=models.PROTECT)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
 
    def __str__(self):
        return f'{self.room_type.name}'

    def is_vacant(self, start_date, end_date):
        bookings = self.booking_set.exclude(check_out_date__lt=end_date, check_in_date__lt=start_date)
        if not bookings.exists():
            return True
        else:
            return False

class CustomerPrice(models.Model):
    adult_price = models.IntegerField(default=100)

class RoomPrice (models.Model):
    price = models.IntegerField(default=700)

class Customer(models.Model):
    age = models.IntegerField(default=18)
    price_per_night = models.ForeignKey(CustomerPrice, on_delete=models.CASCADE)

class Room(models.Model):
    room_price = models.ForeignKey(RoomPrice, on_delete=models.PROTECT, default=1)
    number_of_adult_beds = models.IntegerField(default=1)
    number_of_children_beds = models.IntegerField(default=1)
    max_adults = models.IntegerField(default=1)
    max_children = models.IntegerField(default=1)

class Suite(Room):
    name = 'Suite'

class DoubleRoom(Room):
    name = 'Double'

class SingleRoom(Room):
    name = 'Single'


class Info(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    content = models.CharField(max_length=255)

class Review(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    content = models.CharField(max_length=255)
    class Rating(models.IntegerChoices):
        GREAT = 1
        AMAZING = 2
        AWESOME = 3
    rating = models.IntegerField(choices=Rating.choices)