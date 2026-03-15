from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    role = models.CharField(max_length=20)

    subject = models.CharField(max_length=100,blank=True)

    location = models.CharField(max_length=100,blank=True)

    availability = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.user.username