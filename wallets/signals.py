from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Wallet
from django.contrib.auth import get_user_model

User=get_user_model()

@receiver(post_save, sender=User)
def createWallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(user=instance)