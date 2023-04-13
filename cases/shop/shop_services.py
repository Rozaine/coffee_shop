from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User

from .models import productModel, cardUser, orderModel
from .serializers import orderSerializer

from rest_framework import generics


class orderList(generics.ListAPIView):
    queryset = orderModel.objects.all()
    serializer_class = orderSerializer


def add_to_card(request, product_id):
    card = cardUser()
    card.user = request.user
    card.product_id = productModel.objects.get(product_id=product_id)
    card.save()
    return redirect("/catalog")


def delete_item_card(request, product_id):
    try:
        card_item = cardUser.objects.filter(user=request.user, product_id=product_id)[0]
        card_item.delete()
        return redirect("/card")
    except cardUser.DoesNotExist:
        return redirect("/card")


def get_products():
    return productModel.objects.all()


def get_card(request):
    card = cardUser.objects.filter(user=request.user)
    return card


def get_count_items_in_card(request):
    try:
        product_count = cardUser.objects.filter(user=request.user).count()
        return product_count
    except cardUser.DoesNotExist:
        return 0


def create_order(request):
    if cardUser.objects.filter(user=request.user).count() != 0:
        card_items = cardUser.objects.filter(user=request.user).values()
        order = orderModel()
        items_list = []
        for i in card_items:
            items_list.append(str(i['product_id_id']))
        order.user = request.user
        order.products_id = ",".join(items_list)
        order.order_status = "0"
        order.save()
        card = cardUser()
        product_card = cardUser.objects.filter(user=request.user)
        product_card.delete()
        messages.add_message(request, messages.INFO, "Заказ успешно создан!")
    else:
        messages.add_message(request, messages.INFO, "Корзина пуста!")
    return redirect("/card")
