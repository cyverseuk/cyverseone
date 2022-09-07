from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import VMForm, RequestForm
from django.contrib.auth import login, logout, authenticate
from .models import VM

import inquirer
import pyone

# Create your views here.

def get_session(username, password):
    try:
        one = pyone.OneServer("http://cloud.cis.nbi.ac.uk:2633/RPC2", session=username + ":" + password)
    except pyone.OneAuthenticationException:
        print("Failed to validate user - exiting ...")
        sys.exit(99)
    return one

@login_required(login_url='/login/')
def instantiate_view(request):
	my_form = VMForm(request.POST or None)

	if my_form.is_valid():
		my_form.save()
		#one.template.instantiate(329, my_form.cleaned_data['vmname'])
		my_form = VMForm()
	context = {"form": my_form}
	return render(request, "one/vm_create.html", context)

def sign_up_view(request):
	my_form = RequestForm(request.POST or None)

	if my_form.is_valid():
		user = my_form.save()
		login(request, user)
		return redirect('/instantiate')
	context = {"form": my_form}
	
	return render(request, "registration/sign_up.html", context)


def home_view(request):
	return render(request, "base.html")
