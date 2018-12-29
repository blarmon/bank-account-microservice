from django.shortcuts import render
from rest_framework import viewsets
from .models import BankAccount
from .serializers import BankAccountSerializer


# Create your views here.
class BankAccountView(viewsets.ModelViewSet):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
