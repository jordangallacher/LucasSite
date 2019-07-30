from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Resource(models.Model):
    '''resources available for purchase'''
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    price = models.DecimalField(decimal_places=2, max_digits=7)


class Purchase(models.Model):
    '''purchases'''
    resource = models.ForeignKey(Resource, on_delete=models.PROTECT)
    purchaser = models.ForeignKey(User, on_delete=models.PROTECT)
    purchased_at = models.DateTimeField(auto_now_add=True)
    tx = models.CharField(max_length=250)