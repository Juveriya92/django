from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Story(models.Model):
    title=models.CharField(max_length=150)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    story=models.TextField()
    summary=models.CharField(max_length=250,null=True)
    date_posted=models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.title + '|'+str(self.author)
    
    def get_absolute_url(self):
        return reverse('user_posts')