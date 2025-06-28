from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def login(request,  *args, **kwargs):
    if request.method == 'POST':
        username_or_email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username_or_email, password=password)
        if user is None:
            messages.error(request, 'The user is not registered')
        else:
            login(request, user)
            return redirect('home')
    return render(request, 'registration/login.html')
def home(request):
    return render(request, 'base.html')





