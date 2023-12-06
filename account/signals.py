from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from account.models import UserProfile, Bank

User = get_user_model()



@receiver(post_save, sender=User)
def created_profile(sender, instance, created, **kwargs):
  if created:
    UserProfile.objects.create(user=instance, account_balance=0)
    Bank.objects.create(user=instance)