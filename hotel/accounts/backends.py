from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        NewUser = get_user_model()
        if email is None:
            email = kwargs.get(NewUser.USERNAME_FIELD)
        try:
            user = NewUser._default_manager.get(email = email)
        except NewUser.DoesNotExist:
            NewUser().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
    