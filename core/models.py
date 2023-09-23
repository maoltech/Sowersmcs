from django.db import models
from wallets.models import Wallet
import uuid  
# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstName = models.TextField()
    lastName = models.TextField()
    username = models.TextField(unique=True)
    email = models.CharField()
    phone = models.CharField()
    DOB = models.DateField()
    occupation= models.CharField()
    address = models.CharField()
    LGA = models.CharField()
    country = models.TextField()
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='users', null=True, blank=True)

def __str__(self):
    return self.username


