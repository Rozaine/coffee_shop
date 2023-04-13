from .models import productModel, cardUser
from django.forms import ModelForm


class productForm(ModelForm):
    class Meta:
        model = productModel
        fields = ["name", "price", "calories", "composition", "description", "image"]


