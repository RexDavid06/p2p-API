from django.urls import path
from . import views

urlpatterns = [
    path('transfer/', views.TransferView.as_view()),
    path('ledger/',views.LedgerEntryView.as_view()),
]