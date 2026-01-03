from django.urls import path
from . import views

urlpatterns = [
    path('balance/', views.WalletBalanceView.as_view()),
]