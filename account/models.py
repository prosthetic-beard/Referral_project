from django.db import models
from base.models import TimestampedModel


# Create your models here.
from django.contrib.auth import get_user_model

User = get_user_model()

class UserProfile(TimestampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    account_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class Referral(TimestampedModel):
    referrer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='referrals')
    referred_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class Transactions(TimestampedModel):
    STATUS_TYPES = (
        ('P', 'Pending'),
        ('PC', 'Processing'),
        ('A', 'Approved'),
        ('D', 'Denied'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=(('R','Refferals'), ('W','Withdrawals')))
    amount = models.DecimalField(decimal_places=4, max_digits=15)
    balance = models.DecimalField(decimal_places=4, max_digits=15)
    status = models.CharField(max_length=2, choices=STATUS_TYPES, default="P")
    
    def __str__(self):
        return f'{self.id} - {self.user.email} - {self.amount} - {self.status}'
    


class Bank(TimestampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bank')
    bank_name = models.CharField(max_length=255)
    account_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=255)
    
    
class Coupon(TimestampedModel):
    code = models.CharField(("Coupon Code"), max_length=50)
    
    
    def __str__(self):
        return self.code
    
