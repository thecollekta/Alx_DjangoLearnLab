# social_media_api/accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

# User Model and Authentication
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', 
                                        blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, 
                                       related_name='followers_set')
    following = models.ManyToManyField('self', symmetrical=False, 
                                       related_name='following_set')
    
    def __str__(self):
        return self.username