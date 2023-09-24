from django.db import models
import uuid
from core.models import User
# Create your models here.
class dand(models.Model):
    dandId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    charges = models.DecimalField(max_digits=10, decimal_places=2)
    dandCounts = models.IntegerField()
    description = models.CharField(max_length=250)
    User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dands')


    def __str__(self):
        return self.amount


