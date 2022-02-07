from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass


class Mamoo(models.Model):
    title = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    where = models.CharField(max_length=128, blank=True)
    what = models.TextField(max_length=1024, blank=True)
    when = models.IntegerField()
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='mamoo')

    def __str__(self):
        return self.title
