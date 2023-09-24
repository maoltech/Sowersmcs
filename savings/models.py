from django.db import models
import uuid
from core.models import User
# Create your models here.
class Saving(models.Model):
    savingsId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    savingsCounts = models.IntegerField()
    saver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='savings')
    

    def __str__(self):
        return self.savingsId


