from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from core.utils import generate_uuid_token



class UserRegistrationToken (models.Model):
    '''
    Store user activation tokens.
    '''
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    token = models.UUIDField(default=generate_uuid_token)

    def __str__(self):
        return f"{self.user}'s token"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads', blank=True, null=True)

    def __str__(self):
        return f"{self.user}'s profile"
