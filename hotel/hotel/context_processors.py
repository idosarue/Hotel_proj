from accounts.forms import UserLoginForm


def login_processor(request):
    return {'login_form' : UserLoginForm()}