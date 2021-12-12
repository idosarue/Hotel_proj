from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('logout', views.logout_view, name='logout'),
    path('login', views.UserLoginView.as_view(),name='login'),
]
