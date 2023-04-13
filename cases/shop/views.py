from django.shortcuts import render
from .shop_services import get_products, get_card, get_count_items_in_card


def home(request):
    if request.user.is_authenticated:
        data = {"user": request.user, "count_items": get_count_items_in_card(request)}
    else:
        data = {"user": None, "cards": None, "count_items": 0}
    return render(request, "main/index.html", {"data": data})


def catalog(request):
    if request.user.is_authenticated:
        data = {"user": request.user, "items": get_products(), "count_items": get_count_items_in_card(request)}
    else:
        data = {"user": None, "cards": None, "count_items": 0, "items": get_products()}
    return render(request, "shop/catalog.html", {"data": data})


def about(request):
    if request.user.is_authenticated:
        data = {"user": request.user, "count_items": get_count_items_in_card(request)}
    else:
        data = {"user": None, "cards": None, "count_items": 0}
    return render(request, "main/about.html", {"data": data})


def card(request):
    if request.user.is_authenticated:
        data = {"user": request.user, "cards": get_card(request), "count_items": get_count_items_in_card(request)}
    else:
        data = {"user": None, "cards": None, "count_items": 0}
    return render(request, "shop/card.html", {"data": data})
