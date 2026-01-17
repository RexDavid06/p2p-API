from django.db import models
from django.conf import settings
from uuid import uuid4

User=settings.AUTH_USER_MODEL

# Create your models here.
# class IdempotencyKey(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='idempotency-keys')
#     key = models.UUIDField(default=uuid4, unique=True)

class Transaction(models.Model):
    STATUS_CHOICES = (
        ("PENDING", "Pending"),
        ("FAILED", "Failed"),
        ("SUCCESS", "Success"),
    )
    id = models.UUIDField(default=uuid4, primary_key=True)
    sender = models.ForeignKey(User, on_delete=models.PROTECT, related_name='sent_tnx')
    receiver = models.ForeignKey(User, on_delete=models.PROTECT, related_name='received_tnx')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES)
    idempotency_key = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.id)

