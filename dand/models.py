from django.db import models
import uuid
# Create your models here.
class dand(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    balance = models.DecimalField()
    dandCounts = models.IntegerField()
    description = models.CharField()


def __str__(self):
    return self.username


