from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class LunchGroup(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    pickup_from = models.CharField(max_length = 100)
    departure_time = models.TimeField()
    drop_location = models.CharField(max_length = 100, null=True)
    drop_time = models.TimeField(null = True)
    private = models.BooleanField(default = False)
    invite_code = models.CharField(max_length = 20, null=True)
    status = models.CharField(max_length = 20, default = "Pending")