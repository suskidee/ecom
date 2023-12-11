from django.shortcuts import render, redirect
from .models import Products, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms


# Create your views here.
def home(request):
    products = Products.objects.all()
    category_list = Category.objects.all()
    return render(request, 'home.html', {'products': products, 'category_list': category_list})


def about(request):
    category_list = Category.objects.all()
    return render(request, 'about.html', {'category_list': category_list})


def login_user(request):
    category_list = Category.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, ('you have been logged in'))
            return redirect('home')
        else:
            messages.success(request, ('there was an error. please try again'))
            return redirect('login')
    else:
        return render(request, 'login.html', {'category_list': category_list})


def logout_user(request):
    logout(request)
    messages.success(request, ('you have been logged out'))
    return redirect('home')


def register_user(request):
    form = SignUpForm()
    category_list = Category.objects.all()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ('sign up successful'))
            return redirect('home')
        else:
            messages.success(request, ('there was an error. please try again'))
            return redirect('register')
    else:
        return render(request, 'register.html', {'form': form, 'category_list': category_list})


def category(request, obj):
    obj = obj.replace('-', ' ')
    try:
        category = Category.objects.get(name=obj)
        category_list = Category.objects.all()
        products = Products.objects.filter(category=category)
    except:
        messages.success((request, ('that category does not exist')))
        return redirect('home')
    return render(request, 'category.html',
                  {'products': products, 'category': category, 'category_list': category_list})


def product(request, pk):
    product = Products.objects.get(id=pk)
    category_list = Category.objects.all()

    return render(request, 'product.html', {'product': product, 'category_list': category_list})
