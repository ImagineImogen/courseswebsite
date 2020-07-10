import uuid
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


def generate_token ():
    token = uuid.uuid1()
    return token


class UserRegistrationToken (models.Model):
    '''
    Store user activation tokens.
    '''
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    token = models.UUIDField(default=generate_token)

    def __str__(self):
        return f"{self.user}'s token"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    #image = models.ImageField(default='.jpg')


# @receiver(post_save, sender = User)
# def save_profile (sender, instance, **kwargs):
#     print(instance.profile)
#     instance.profile.save()
