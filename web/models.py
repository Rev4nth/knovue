from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_text =  models.TextField()
    time_stamp = models.DateTimeField(auto_now=True)
