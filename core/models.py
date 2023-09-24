from django.db import models
from wallets.models import Wallet
import uuid  
# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstName = models.TextField(max_length=100)
    lastName = models.TextField(max_length=100)
    username = models.TextField(unique=True, max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    DOB = models.DateField(max_length=20)
    occupation= models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    LGA = models.CharField(max_length=100)
    country = models.TextField(max_length=100)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='users', null=True, blank=True)
    image = models.ImageField(upload_to='user_image', default='blank-user-image.png')

def __str__(self):
    return self.username


