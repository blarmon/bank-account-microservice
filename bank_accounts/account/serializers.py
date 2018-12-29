from rest_framework import serializers
from .models import BankAccount

class BankAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankAccount
        fields = ('id', 'customer', 'account_type', 'balance', 'interest_rate', 'account_opened')
