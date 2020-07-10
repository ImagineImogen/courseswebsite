from django.urls import path
from . views import *


urlpatterns = [
    path('register', signup, name="signup"),
    path('user/activation',activation, name="activation"),
    path('test', activation, name='test'),
]