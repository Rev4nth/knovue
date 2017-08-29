from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from taggit.managers import TaggableManager
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=140)
    text =  models.TextField()
    image = models.ImageField(null=True)
    created = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='likes')
    tags = TaggableManager()

    def total_likes(self):
        return self.likes.count()

    def is_liked(self):
        return self.likes.filter(id=self.user.id).exists()

    class Meta:
           ordering = ('-created',)

    def __str__(self):
        return self.title + ", " + self.text
