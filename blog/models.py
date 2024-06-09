from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
import os
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User


def validate_min_length(value):
    if len(value) < 5:
        raise ValidationError('The title must be at least 5 characters long.')
def validate_rating(value):
    if not bool(value):
        raise ValidationError('Please provide a rating.')
    elif value > 5 or value < 1:
        raise ValidationError('Rate on a scale of 1 to 5')
class UserReview(models.Model):
    reviewId = models.AutoField(primary_key = True)
    breweryId = models.CharField(max_length=120)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    userName = models.CharField(max_length=150)
    description = models.TextField(max_length=1000, validators=[
            MinLengthValidator(50, 'Your review must be atleast 50 characters long.')
            ]
        )
    rate = models.IntegerField(validators=[validate_rating])  
    check_field = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('breweryId', 'userId')

    def __str__(self):
        return str(self.userName) +"BreweryId "+str(self.breweryId)
        
