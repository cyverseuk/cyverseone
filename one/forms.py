from django import forms
from .models import VM, UserQuota

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class VMForm(forms.ModelForm):
	class Meta:
		model = VM
		fields = [
			'ram',
			'storage',
			'cpu',
			'vmname',
			'key',
			'username',
		]

class RequestForm(UserCreationForm):
	email = forms.EmailField(required=True)
	affiliation = forms.CharField(required=True)
	class Meta:
		model = User
		fields = ["username", "email", "affiliation","password1", "password2"]
