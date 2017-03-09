from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from taggit.managers import TaggableManager
# Create your models here.

class Post(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_text =  models.TextField()
    created = models.DateTimeField(auto_now=True)
    tags = TaggableManager()

    class Meta:
           ordering = ('-created',)

    def __str__(self):
        return self.post_text
