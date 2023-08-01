from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from .models import *


def home(request):
    user = User.objects.all()
    articles = Articles.objects.all()
    return render(request, "home.html", {"articles": articles, "users": user})


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are logged In")
            return redirect("home")
        else:
            messages.success(request, "Error while logging")
            return redirect("home")
    else:
        return redirect("home")


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect("home")


def register_user(request):
    try:
        if request.method == "POST":
            form = SignUpForm(request.POST)

            if form.is_valid():
                form.save()

            # username = form.cleaned_data["username"]
            # password = form.cleaned_data["password1"]
            # user = authenticate(username=username, password=password)
            # login(request, user)
            messages.success(request, "You have successfully registered")
            return redirect("home")
        else:
            form = SignUpForm()
            
            return render(request, "register.html", {"form": form})
    except Exception as e:
        print(e)


def delete_user(request, pk):
    if request.user.is_authenticated:
        delete_it = User.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Deleted ")
        return redirect("home")
    else:
        messages.success(request, "Login to delete record")
        return render("home")
