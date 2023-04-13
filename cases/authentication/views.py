from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from shop.shop_services import get_count_items_in_card
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout as LogOut
from shop.forms import productForm


def signup(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Аккаунт успешно создан")
            return redirect("/signin")
        else:
            messages.info(request, "что-то не так")

    data = {'form': form}
    return render(request, "authentications/signup.html", data)


def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Bad info")
    return render(request, "authentications/signin.html")


def logout(request):
    LogOut(request)
    return redirect("/")


def profile(request):
    form = productForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("/profile")
    data = {"user": request.user, "count_items": get_count_items_in_card(request), "form": form}
    return render(request, "authentications/profile.html", {"data": data})
