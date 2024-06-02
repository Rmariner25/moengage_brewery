from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
import os


class UserReview(models.Model):
    reviewId = models.AutoField(primary_key = True)
    breweryId = models.CharField(max_length=120)
    userName = models.CharField(max_length=120)
    description = models.TextField(max_length=500)
    rate = models.IntegerField(default=0)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.userName) + str(self.created_at)
        
