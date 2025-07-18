from django.contrib.auth import login, authenticate, get_user_model
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout

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



def user_login(request, *args, **kwargs):
    if request.method == 'POST':
        username_or_email = request.POST.get('email')
        password = request.POST.get('password')

        User = get_user_model()
        user = None

        if '@' in username_or_email:
            try:
                user_obj = User.objects.get(email=username_or_email)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                messages.error(request, 'No user found with this email.')
                return redirect('login')
            except User.MultipleObjectsReturned:
                messages.error(request, 'Multiple users found with this email. Please contact support.')
                return redirect('login')
        else:
            user = authenticate(request, username=username_or_email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
            return redirect('login')

    return render(request, 'registration/login.html')


def home(request):
    return render(request, 'base.html')

def create_quiz(request):
    return render(request, 'create_quiz.html')

def logout_user(request):
    logout(request)  # This logs out the user
    return redirect('home')




