from django.db import models
from core.models import User
import uuid
# Create your models here.
class Shares(models.Model):
    sharesId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sharesCounts = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shares')
    
def __str__(self):
    return self.price


