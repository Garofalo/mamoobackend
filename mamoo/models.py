from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Mamoo(models.Model):
    title = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    where = models.CharField(max_length=128)
    what = models.TextField(max_length=1024)
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='mamoo')

    def __str__(self):
        return self.title
