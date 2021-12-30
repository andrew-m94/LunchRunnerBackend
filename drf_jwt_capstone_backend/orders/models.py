from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Order(models.Model):
    lunchgroup = models.ForeignKey('lunchgroups.LunchGroup', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    order_content = models.CharField(max_length = 500)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    notes = models.CharField(max_length = 500, null=True)

