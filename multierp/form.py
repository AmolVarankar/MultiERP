from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms

from .models import Muser, Order

class CreateOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['product','company','status','sales_registration']

class UpdateOrderForm1(ModelForm):
        class Meta:
            model = Order
            fields = ['product','company','status','operation_handler',]
            #fields = ['product','company','status','sales_registration','operation_handler',]

class UpdateOrderForm2(ModelForm):
        class Meta:
            model = Order
            fields = ['product','company','status','finance_handler',]
            #fields = ['product','company','status','sales_registration','operation_handler','finance_handler',]

class UpdateOrderForm3(ModelForm):            
        class Meta:
            model = Order
            fields = ['product','company','status','shipping_handler',]
            #fields = ['product','company','status','sales_registration','operation_handler','finance_handler','shipping_handler',]

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
