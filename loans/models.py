from django.db import models
from core.models import User
import uuid
# Create your models here.
class Loan(models.Model):
    loanId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    rate = models.IntegerField()
    expireDate = models.DateField()
    loaner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='loans')
    

def __str__(self):
    return self.loanId


