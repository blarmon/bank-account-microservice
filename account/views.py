from django.shortcuts import render
from rest_framework import viewsets
from .models import BankAccount
from django.contrib.auth.models import User
from .serializers import BankAccountSerializer, UserSerializer


# Create your views here.
class BankAccountView(viewsets.ModelViewSet):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer(partial=True)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer(partial=True)
