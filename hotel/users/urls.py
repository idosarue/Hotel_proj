from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.Home.as_view(), name='home'),
    path('rooms', views.RoomsResults.as_view(), name='rooms'),
]
