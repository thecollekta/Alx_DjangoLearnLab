# blog/models.py

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

# Blog Post 
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
# User Profile
class Profile(models.Model):
       user = models.OneToOneField(User, on_delete=models.CASCADE)
       bio = models.TextField(max_length=500, blank=True)
       location = models.CharField(max_length=30, blank=True)
       birth_date = models.DateField(null=True, blank=True)

       def __str__(self):
           return f'{self.user.username} Profile'
    
# Blog Comment System
class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'