from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from account.models import Bank


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={'class': "form-control", 'type': 'email', "placeholder": "Enter email address", "id":"exampleInputEmail1"}))
	firstname = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': "form-control", 'type': 'text', "placeholder": "Enter firstname", "id":"firstName"}))
	lastname = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': "form-control", 'type': 'text', "placeholder": "Enter lastname", "id":"lastName"}))
	phone = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': "form-control", 'type': 'phone',"placeholder": "Enter phone", "id":"phone"}))
	password1 = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': "form-control", 'type': 'password', "placeholder": "•••••••••", "id":"exampleInputPassword1"}))
	password2 = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': "form-control", 'type': 'password', "placeholder": "•••••••••", "id":"exampleInputPassword2"}))
	referral_code = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': "form-control", 'type': 'phone',"placeholder": "Enter refferral code", "id":"ref", "disabled":True}))

	class Meta:
		model = get_user_model()
		fields = ("email", "firstname", "lastname",  "phone", "password1", "password2", "referral_code")

	# def save(self, commit=True):
	# 	user = super(NewUserForm, self).save(commit=False)
	# 	user.email = self.cleaned_data['email']
	# 	if commit:
	# 		user.save()
	# 	return user
	

class LoginForm(forms.Form):
    email = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': "form-control", "placeholder": "Enter email address", "id":"exampleInputEmail1"}))
    password = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': "form-control", 'type': 'password', "placeholder": "•••••••••", "id":"exampleInputPassword1"}))
    

class WithdrawalForm(forms.Form):
    amount = forms.CharField(required=True, widget=forms.NumberInput(
        attrs={'class': "form-control inputted-amount", "placeholder": "0.00", "id":"Amount"}))
    
    
class CouponForm(forms.Form):
	code = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': "form-control inputted-amount", "placeholder": "Enter Coupon code", "id":"Amount"}))
 
 
class BankForm(forms.ModelForm):
    bank_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control", "placeholder": "Enter bank name", "id":"exampleInputEmail1"}))
    account_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control", "placeholder": "Enter account name", "id":"exampleInputEmail1"}))
    account_number = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': "form-control", "placeholder": "Enter account number", "id":"exampleInputEmail1"}))
    
    class Meta:
        model = Bank
        exclude = ["user"]

    