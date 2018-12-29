from rest_framework import serializers
from .models import BankAccount
from django.contrib.auth.models import User


class BankAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankAccount
        fields = ('id', 'customer', 'account_type', 'balance', 'interest_rate', 'account_opened')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'accounts')