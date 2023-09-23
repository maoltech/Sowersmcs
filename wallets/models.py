from django.db import models

# Create your models here.
class Wallet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    balance = models.DecimalField()
    transactionCounts = models.IntegerField()
    

def __str__(self):
    return self.username


