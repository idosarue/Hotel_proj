
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotel.settings')
django.setup()

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

print(get_user_model())
print(User)