from django.db import models
from base.models import TimestampedModel


# Create your models here.
from django.contrib.auth import get_user_model

User = get_user_model()

class UserProfile(TimestampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    account_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return self.user.email

class Referral(TimestampedModel):
    referrer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='referrals')
    referred_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f'{self.referrer} - {self.referred_user}'
    
    @property
    def referrer_balance(self):
        return self.referrer.account_balance
    
    @property
    def referred_user_balance(self):
        return self.referred_user.account_balance


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
    
    def save(self, *args, **kwargs):
        user_profile = UserProfile.objects.get(user=self.user)
        if self.type == 'W' and self.status == 'A':
            user_profile.account_balance = self.balance
            user_profile.save()
        super(Transactions, self).save(*args, **kwargs)
    


class Bank(TimestampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bank')
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    account_name = models.CharField(max_length=255, blank=True, null=True)
    account_number = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.user.email
    
    
class Coupon(TimestampedModel):
    code = models.CharField(("Coupon Code"), max_length=50)
    
    
    def __str__(self):
        return self.code
    
