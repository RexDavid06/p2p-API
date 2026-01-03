from django.contrib import admin
from .models import Transaction

# Register your models here.
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'amount', 'status']


admin.site.register(Transaction, TransactionAdmin)
