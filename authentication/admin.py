from django.contrib import admin
from .models import User
# Register your models here.
class CustomAdmin(admin.ModelAdmin):
    list_display =['email', 'firstname', 'lastname','phone','is_vip', 'created_at']
    search_fields = ('email',)
    list_filter =['is_vip', ]
    
    

admin.site.register(User, CustomAdmin)