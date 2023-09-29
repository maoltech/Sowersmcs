from django.db import models
from wallets.models import Wallet
import uuid  
# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstName = models.TextField(max_length=100)
    lastName = models.TextField(max_length=100)
    password = models.CharField(max_length=250, default="1234")
    username = models.TextField(unique=True, max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    DOB = models.DateField(max_length=20, null=True)
    occupation= models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    LGA = models.CharField(max_length=100)
    country = models.TextField(max_length=100)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='users', null=True, blank=True)
    image = models.ImageField(upload_to='user_image', default='blank-user-image.png')

    def __str__(self):
        return self.username

class Loan(models.Model):
    loanId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    rate = models.IntegerField()
    expireDate = models.DateField()
    loaner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='loans')
    

    def __str__(self):
        return self.loanId
    
class dand(models.Model):
    dandId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    charges = models.DecimalField(max_digits=10, decimal_places=2)
    dandCounts = models.IntegerField()
    description = models.CharField(max_length=250)
    User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dands')


    def __str__(self):
        return self.amount

class Saving(models.Model):
    savingsId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    savingsCounts = models.IntegerField()
    saver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='savings')
    

    def __str__(self):
        return self.savingsId
    
class Share(models.Model):
    sharesId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sharesCounts = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shares')
    
    def __str__(self):
        return self.price

