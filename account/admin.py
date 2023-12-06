from django.contrib import admin
from .models import UserProfile, Referral, Transactions, Bank, Coupon
# Register your models here.

class TransactionAdmin(admin.ModelAdmin):
    add_form=Transactions
    list_display =['id', 'user_email', 'type', 'amount','balance','status', 'created_at']
    search_fields = ('user__email',)
    list_filter =['type', 'status']
    
    def user_email(self, obj):
        return str(obj.user.email)
    
    
class BankAdmin(admin.ModelAdmin):
    list_display =['user', 'bank_name', 'account_name','account_number', 'created_at']
    search_fields = ('user',)
    list_filter =['user', ]

admin.site.register(UserProfile)
admin.site.register(Referral)
admin.site.register(Transactions, TransactionAdmin)
admin.site.register(Bank, BankAdmin)
admin.site.register(Coupon)