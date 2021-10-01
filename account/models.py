from django.db import models
from django.contrib.auth.models import User 
from heart.models import Heart
from kidney.models import *
from Diabetes.models import *
# Create your models here.
class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="profile")
    photo=models.ImageField(upload_to="uploads",null=True, blank=True)
    phone=models.CharField(max_length=20,null=True, blank=True)
    heart=models.ManyToManyField(Heart,related_name="heart_data",null=True, blank=True)
    kidney=models.ManyToManyField(Kidney,related_name="kidney_data",null=True, blank=True)
    diabetes=models.ManyToManyField(Diabets,related_name="diabetes_data",null=True, blank=True)

    def __str__(self):
        return str(self.user)