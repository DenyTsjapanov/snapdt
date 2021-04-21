from django.shortcuts import render, get_object_or_404
from .models import Item

# Create your views here.


def all_items(request):

    items = Item.objects.all()

    context = {
        'items': items,
    }

    return render(request, 'portfolio/portfolio.html', context)


def item_detail(request, item_id):

    item = get_object_or_404(Item, pk=item_id)

    context = {
        'item': item,
    }

    return render(request, 'portfolio/item_detail.html', context)
