from django.db import models
from django.contrib.auth.models import User


class productModel(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    price = models.CharField(max_length=100)
    calories = models.CharField(max_length=10)
    composition = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/', null=True, max_length=255)


class cardUser(models.Model):
    card_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(productModel, on_delete=models.CASCADE)


class orderModel(models.Model):
    order_id = models.AutoField(primary_key=True)
    time_create = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products_id = models.CharField(max_length=100)
    order_status = models.CharField(max_length=2)