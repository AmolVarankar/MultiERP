from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms

from .models import *

class CreateSalesOrderForm(ModelForm):
    class Meta:
        model = SalesOrder
        fields = '__all__'
        exclude= ['Status']

class UpdateSalesOrderForm(ModelForm):
        class Meta:
            model = SalesOrder
            fields = '__all__'
            

class CreatePurchaseOrderForm(ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'
        exclude= ['Status']

class UpdatePurchaseOrderForm(ModelForm):
        class Meta:
            model = PurchaseOrder
            fields = '__all__'

class SignUpForm(UserCreationForm):

    USER_TYPE_CHOICES = ( 
		('Sal', 'Sales'),
		('Opn', 'Operations'),
		('Fin', 'Finance'),
		('Adm', 'Admin'),)

    username = forms.CharField(widget=forms.TextInput)
    first_name = forms.CharField(widget=forms.TextInput, max_length=32, help_text='First name')
    last_name=forms.CharField(widget=forms.TextInput, max_length=32, help_text='Last name')
    email=forms.EmailField(widget=forms.EmailInput, max_length=64, help_text='Enter a valid email address')
    password1=forms.CharField(widget=forms.PasswordInput)
    password2=forms.CharField(widget=forms.PasswordInput)
    user_type=forms.Select(choices=USER_TYPE_CHOICES)

    class Meta(UserCreationForm.Meta):
        model = Muser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email','user_type')            

class SearchItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

class CreateItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["item_code","item_description","item_name","item_type","item_category","item_group","alternate_sw_code","site","HSN_code"]

class UpdateItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

class SearchPartyForm(ModelForm):
    class Meta:
        model = Party
        fields = '__all__'

class CreatePartyForm(ModelForm):
    class Meta:
        model = Party
        fields = '__all__'
        exclude = ['Status']

class UpdatePartyForm(ModelForm):
    class Meta:
        model = Party
        fields = '__all__'

