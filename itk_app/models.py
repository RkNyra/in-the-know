from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phone_field import PhoneField
from pyuploadcare.dj.models import ImageField

#User/Profile Model
class Profile(models.Model):
    prof_pic = ImageField(blank=True, manual_crop="", null=True)
    bio = models.CharField(max_length = 250, null=True)
    email = models.EmailField()
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE, null=True)
    user = models.OneToOneField('auth.User',on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.user)
    
    def save_profile(self):
        self.save()