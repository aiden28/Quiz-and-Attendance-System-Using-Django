from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ContactUs
from college import views




# Create your views here.

def home(request):
    count = User.objects.count()
    return render(request, 'base.html', {'count': count})


def signup(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			return redirect('home')
	else:
		form=UserCreationForm()
	return render(request, 'registration/signup.html', {'form':form})

def contactUs(request):
	obj=ContactUs()
	obj.name=request.POST.get('name')
	obj.email=request.POST.get('email')
	obj.subject=request.POST.get('subject')
	obj.message=request.POST.get('message')
	obj.save()
	return redirect(home)


