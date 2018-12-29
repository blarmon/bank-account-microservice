from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class BankAccount(models.Model):

    customer_id = models.ForeignKey(User,on_delete=models.CASCADE,)
    account_type = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=8, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=2, decimal_places=2)
    account_opened = models.DateTimeField(default=datetime.now())

    def is_overdrawn(self):
        if self.balance < 0:
            return True
        return False

    def get_account_age(self):
        return datetime.now() - self.account_opened
