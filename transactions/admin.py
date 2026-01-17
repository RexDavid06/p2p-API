from django.contrib import admin
from .models import Transaction, LedgerEntry

# Register your models here.
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'amount', 'status']


class LedgerEntryAdmin(admin.ModelAdmin):
    list_display = ['transaction', 'amount', 'entry_type', 'date_created']


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(LedgerEntry, LedgerEntryAdmin)
