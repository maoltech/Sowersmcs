from django.db import models
# from wallets.models import Wallet  
# Create your models here.
class User(models.Model):
    id = models.IntegerField()
    firstName = models.TextField()
    lastName = models.TextField()
    username = models.TextField()
    email = models.CharField()
    phone = models.CharField()
    DOB = models.DateField()
    occupation= models.CharField()
    address = models.CharField()
    LGA = models.CharField()
    country = models.TextField()

#wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='users', null=True, blank=True)

def __str__(self):
    return self.username


