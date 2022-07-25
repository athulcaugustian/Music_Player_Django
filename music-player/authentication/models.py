from django.db import models  
from django.contrib.auth.models import AbstractUser

#Create your models here.
class CustomUser(AbstractUser):
    is_user= models.BooleanField(default=True)
    is_artist= models.BooleanField(default=False)


    