from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from bootstrap_datepicker_plus import DatePickerInput

from .models import Profile

class SignUpForm(UserCreationForm):
	email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')		

class UserForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email']

class ProfileForm(forms.ModelForm):

	class Meta:
		model = Profile
		fields = ['birth_date', 'phone_number']
		widgets = {
			'birth_date': DatePickerInput(format='%Y-%m-%d'),
		}