from decimal import Decimal
from django.db import transaction
from wallets.models import Wallet
from .models import Transaction, LedgerEntry


class InsufficientFunds(Exception):
    pass


@transaction.atomic
def transfer_funds(*, sender, receiver, amount, idempotency_key):
    if Transaction.objects.filter(idempotency_key=idempotency_key).exists():
        return Transaction.objects.get(idempotency_key=idempotency_key)
    
    sender_wallet = Wallet.objects.select_for_update().get(user=sender)
    receiver_wallet = Wallet.objects.select_for_update().get(user=receiver)

    if sender_wallet.balance < amount:
        raise InsufficientFunds("Insufficient Balance")
    
    sender_wallet.balance -= Decimal(amount)
    receiver_wallet.balance += Decimal(amount)

    sender_wallet.save()
    receiver_wallet.save()

    tx = Transaction.objects.create(
        sender=sender,
        receiver=receiver,
        amount=amount,
        status='SUCCESS',
        idempotency_key=idempotency_key,
    )
    # ledger entry
    LedgerEntry.objects.bulk_create([
        LedgerEntry(
            transaction=tx,
            wallet=sender_wallet,
            amount=amount,
            entry_type="DEBIT",
        ),
        LedgerEntry(
            transaction=tx,
            wallet=receiver_wallet,
            amount=amount,
            entry_type="CREDIT",
        )
    ])
    return tx
