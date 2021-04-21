from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.all_items, name='items'),
    path('<item_id>', views.item_detail, name='item_detail'),
]
