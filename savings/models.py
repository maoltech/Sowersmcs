from django.db import models
import uuid
# Create your models here.
class Savings(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    balance = models.DecimalField()
    savingsCounts = models.IntegerField()
    

def __str__(self):
    return self.username


