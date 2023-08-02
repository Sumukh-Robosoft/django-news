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


def add_article(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddArticles(request.POST, request.FILES)
            if form.is_valid():
                add_article = form.save(commit=False)
                add_article.author = request.user
                add_article.status = "DRAFT"
                add_article.save()
                messages.success(request, "Article added")
                return redirect('home')
            else:
                print(form.errors)
        else:
            form = AddArticles()
        return render(request, 'add_article.html', {'form': form})
    else:
        messages.success(request, "Login to add record")
        return redirect('home')

def individual_article(request,pk):
    if request.user.is_authenticated:
        article = Articles.objects.get(id=pk)
        return render(request, 'article.html', {'article':article})
    else:
        messages.success(request,"Login to view record")
        return render('home')




def view_articles(request):
    current_user = request.user.id
    user = User.objects.get(id = current_user)
    articles = Articles.objects.filter(author =user)
    return render(request, "articles.html", {"articles": articles})




    
    


def edit_article(request,pk):
    if request.user.is_authenticated:
        current_record = Articles.objects.get(id=pk)
        if current_record.status == "PUBLISHED":
            messages.success(request,"Published article cannot be edited")
            return redirect('home')
        form = AddArticles(request.POST  or None,instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,"article updated")
            return redirect('home')
        return render(request,'edit_article.html',{'form':form})
    else:
        messages.success(request,"Login to update record")
        return render('home')



def publish_article(request,pk):
    current_record = Articles.objects.get(id=pk)
    if current_record.status == "PUBLISHED":
        messages.success(request,"Already published")
        return redirect('home')
    current_record.publisher = request.user
    current_record.status = "PUBLISHED"
    current_record.save()
    return redirect('home')