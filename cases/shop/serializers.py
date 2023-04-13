from rest_framework import serializers
from .models import orderModel


class orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = orderModel
        fields = ["order_id", "time_create", "user", "products_id",  "order_status"]
