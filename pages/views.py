from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from blogs.models import Category, Blog
from courses.models import Course
from pages.forms import SignUpForm, EditProfile
from pages.models import About


def index(request):
    categories = Category.objects.filter(featured=True)[:4]
    blog_recent = Blog.objects.order_by('-publish_date_now')[:6]
    return render(request, 'pages/index.html', {'categories': categories, 'blog_recent': blog_recent})


def about(request):
    about = About.objects.all()
    return render(request, 'pages/about_us.html', {'about': about})


def contact(request):
    return render(request, 'pages/contact.html', {})


def privacy(request):
    return render(request, 'pages/privacy.html', {})


def financial_support(request):
    return render(request, 'pages/financial_support.html', {})


def terms(request):
    return render(request, 'pages/terms.html', {})

    #############  AUTHRNTICATION FUNCTIONS STARTS  ##############


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You Have been Log In')
            return redirect('/')
        else:

            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def user_logout(request):
    logout(request)
    messages.success(request, 'You Successfuly LogOut see You soon!')
    return redirect('home')


def signup_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'You Have been Resgisted Successfuly')
            return redirect('home')


    else:
        form = SignUpForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfile(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'You Have been Edited successfuly')
            return redirect('home')

    else:
        form = EditProfile(instance=request.user)

    context = {
        'form': form
    }

    return render(request, 'accounts/profile.html', context)


def edit_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'You Have been Changed Password successfuly')
            return redirect('home')

    else:
        form = PasswordChangeForm(user=request.user)

    context = {
        'form': form
    }

    return render(request, 'accounts/password.html', context)
