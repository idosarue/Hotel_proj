from sys import is_finalizing
from django.db import models
from accounts.models import Profile


# Create your models here.
class Booking(models.Model):
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    rooms = models.ManyToManyField('Room')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    is_approved = models.BooleanField(default=False)
    # def __str__(self):
    #     return f'{self.room_type.name}'

    # def is_vacant(self, start_date, end_date):
    #     bookings = self.booking_set.exclude(check_out_date__lt=end_date, check_in_date__lt=start_date)
    #     if not bookings.exists():
    #         return True
    #     else:
    #         return False

class CustomerPrice(models.Model):
    adult_price = models.IntegerField(default=100)

class RoomPrice (models.Model):
    price = models.IntegerField(default=700)

    def __str__(self):
        return f'{self.price}'

class RoomType(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=255)

class Customer(models.Model):
    age = models.IntegerField(default=18)
    price_per_night = models.ForeignKey(CustomerPrice, on_delete=models.CASCADE)


class Room(models.Model): 
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    room_price = models.ForeignKey(RoomPrice, on_delete=models.PROTECT, default=1)
    number_of_adult_beds = models.IntegerField(default=1)
    number_of_children_beds = models.IntegerField(null=True)
    max_adults = models.IntegerField(default=1)
    max_children = models.IntegerField(null=True)

    # def __str__(self):
    #     return f'{self.room_type.name, self.room_price.price, self.number_of_adult_beds, self.number_of_children_beds}'

    def is_vacant(self, start_date, end_date):
        if self.booking_set.filter(check_out_date__gt=start_date, check_in_date__lt=end_date, is_approved=True).exists():
            return False
        return True



# check out = 2021-12-22, start = 2021-12-21
# check in = 2021-12-11, end = 2021-12-10



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