from django.contrib import admin
from .models import UserProfile, Referral, Transactions, Bank
# Register your models here.



admin.site.register(UserProfile)
admin.site.register(Referral)
admin.site.register(Transactions)
admin.site.register(Bank)