from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
import os
from django.core.validators import MinLengthValidator


def validate_min_length(value):
    if len(value) < 5:
        raise ValidationError('The title must be at least 5 characters long.')
    
class UserReview(models.Model):
    reviewId = models.AutoField(primary_key = True)
    breweryId = models.CharField(max_length=120)
    userName = models.CharField(max_length=150)
    title = models.CharField(max_length=150, validators=[validate_min_length])
    description = models.TextField(max_length=1000, validators=[
            MinLengthValidator(50, 'The field must contain at least 50 characters')
            ]
        )
    rate = models.IntegerField(default=0)  
    check_field = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('breweryId', 'userName')

    def __str__(self):
        return str(self.userName) +"title: "+str(self.title)
        
