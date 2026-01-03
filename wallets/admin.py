from django.contrib import admin
from .models import Wallet

# Register your models here.
class WalletAdmin(admin.ModelAdmin):
    list_display = ['user', 'balance', 'created_at']

admin.site.register(Wallet, WalletAdmin)

