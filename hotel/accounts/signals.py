from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile, NewUser

@receiver(post_save, sender=NewUser)
def create_user(sender, instance , created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
