from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LogInForm
from django.contrib import messages


# Create your views here.

def signup(request):
    if not request.user.is_authenticated:
        form = RegisterForm()
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, "Your account has been created successfully!")
        else:
            form = RegisterForm()
        return render(request, 'auth/signup.html', {'form': form, 'signup': 'active'})
    else:
        return HttpResponseRedirect('')


def userlog(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LogInForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.add_message(request, messages.SUCCESS, "You've successfully logged in")
                    return redirect('/')
        else:
            form = LogInForm()
        return render(request, 'auth/login.html', {'form': form, 'login': 'active'})
    else:
        return HttpResponseRedirect('/')


def log_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/login/')
