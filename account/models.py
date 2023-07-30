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
    referred_user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)