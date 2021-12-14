from django.db import models
from accounts.models import Profile


# Create your models here.
class Booking(models.Model):
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    room = models.ForeignKey('Room', on_delete=models.PROTECT)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)


class CustomerPrice(models.Model):
    adult_price = models.IntegerField(default=100)

class RoomPrice (models.Model):
    price = models.IntegerField(default=700)

class Customer(models.Model):
    age = models.IntegerField(default=18)
    price_per_night = models.ForeignKey(CustomerPrice, on_delete=models.CASCADE)

class RoomType(models.Model):
    name = models.CharField(max_length=40)
    price_per_night = models.ForeignKey(RoomPrice, on_delete=models.CASCADE, default=1)

class Room(models.Model):
    room_type = models.ForeignKey(RoomType, on_delete=models.PROTECT)

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