from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
  #Boolean fields to select the type of account.
  is_paitent = models.BooleanField(default=False)
  is_doctor = models.BooleanField(default=False)

class Paitent(models.Model):
    paitent = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length = 255)
    email = models.EmailField(db_index=True,unique=True)
    age = models.IntegerField()
    sex = models.CharField(max_length = 40)
    case = models.TextField()
    cell_number_one = models.CharField(max_length = 40)

    def __str__(self):
        return self.paitent.username

class Doctor(models.Model):
    doctor = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True, null=True)
    name = models.CharField(max_length = 255)
    email = models.EmailField(db_index=True,unique=True)

    def __str__(self):
        return self.doctor.username