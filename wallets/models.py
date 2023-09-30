from django.db import models
import uuid
# Create your models here.
class Wallet(models.Model):
    walletId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    balance = models.DecimalField(max_digits=50, decimal_places=2)
    transactionCounts = models.IntegerField()
    accountNo = models.IntegerField(default=123456789)
    bank = models.TextField(max_length=100, default="Bank")
    accountName = models.CharField(max_length=100, default="account name")


    def __dec__(self):
        return self.balance


