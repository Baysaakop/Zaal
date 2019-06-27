from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.forms import modelformset_factory
from django.http import JsonResponse

from .forms import SignUpForm, UserForm, ProfileForm
from courts.models import Court, CourtPhoto
from courts.forms import CourtForm, AddressForm

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():		
			user = form.save()
			auth_login(request, user)
			return redirect('home')
	else:
		form = SignUpForm()
	return render(request, 'registration/signup.html', {'form': form})

@login_required
def account(request):
	user_form = UserForm(instance=request.user)
	profile_form = ProfileForm(instance=request.user.profile)
	if request.method == 'POST':
		user_form = UserForm(request.POST, instance=request.user)
		profile_form = ProfileForm(request.POST, instance=request.user.profile)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()				
	return render(request, 'profile/account.html', {
		'user_form': user_form,
		'profile_form': profile_form
	})