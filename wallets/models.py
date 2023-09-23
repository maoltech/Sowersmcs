from django.db import models
import uuid
# Create your models here.
class Wallet(models.Model):
    walletId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    transactionCounts = models.IntegerField()


def __str__(self):
    return self.balance


