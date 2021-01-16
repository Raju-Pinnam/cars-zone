from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import (get_user_model, authenticate,
                                 login as login_user, logout as logout_user)

User = get_user_model()


# Create your views here.
def login(request):
    if request.method == "POST":
        data = request.POST
        username = data['username']
        password = data['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login_user(request, user)
            return redirect('accounts:dashboard')
        else:
            messages.error(request, "Check your password")
    return render(request, 'accounts/login.html')


def register(request):
    if request.method == "POST":
        data = request.POST
        firstname = data['firstname']
        lastname = data['lastname']
        username = data['username']
        password = data['password']
        confirm_password = data['confirm_password']
        email = data['email']
        # password checking
        if password == confirm_password:
            # user name checking
            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    user = User.objects.create_user(first_name=firstname, last_name=lastname,
                                                    username=username, email=email)
                    user.set_password(password)
                    user.save()
                    messages.success(request, 'Welcome to family')
                else:
                    messages.error(request, 'Email is already exists')
            else:
                messages.error(request, 'Username already exists')
        else:
            messages.error(request, 'Password mismatch')

    return render(request, 'accounts/register.html')


def logout(request):
    if request.user.is_authenticated:
        logout_user(request)
        return redirect('accounts:login')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
