from django.db import models
import uuid
from core.models import User
# Create your models here.

class transaction(models.Model):
    transactionId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField()
    transactor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User')
    