from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views, shop_services

from rest_framework.urlpatterns import format_suffix_patterns

app_name = "shop"

urlpatterns = [
                  path("", views.home, name="home"),
                  path("catalog", views.catalog, name="catalog"),
                  path("about", views.about, name="about"),
                  path("catalog/<int:product_id>/", shop_services.add_to_card, name="ticket_page"),
                  path("card", views.card, name="card"),
                  path("card/delete/<int:product_id>", shop_services.delete_item_card, name="delete_item_card"),
                  path("card/create_order", shop_services.create_order, name="create_order"),
                  path("orders/", shop_services.orderList.as_view())
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
