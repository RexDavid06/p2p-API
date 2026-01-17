from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .serializers import TransferSerializer, LedgerEntrySerializer
from .services import transfer_funds
from rest_framework.response import Response
from .models import LedgerEntry
from rest_framework.generics import ListAPIView

User=get_user_model()

# Create your views here.
class TransferView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = TransferSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        receiver = User.objects.get(id=serializer.validated_data['receiver_id'])

        tx = transfer_funds(
            sender=request.user,
            receiver=receiver,
            amount=serializer.validated_data['amount'],
            idempotency_key=serializer.validated_data['idempotency_key'],
        )

        return Response({
            "transaction_id": tx.id,
            "status": tx.status
        })


class LedgerEntryView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LedgerEntrySerializer

    def get_queryset(self):
        return LedgerEntry.objects.filter(wallet__user=self.request.user).select_related("transaction").order_by("date_created")

        
