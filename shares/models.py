from django.db import models
from core.models import User
import uuid
# Create your models here.
class Shares(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    balance = models.DecimalField()
    sharesCounts = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='loans')
    
def __str__(self):
    return self.username


