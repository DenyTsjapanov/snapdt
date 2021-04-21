from django.shortcuts import render
from .models import Item

# Create your views here.


def all_items(request):

    items = Item.objects.all()

    context = {
        'items': items,
    }

    return render(request, 'portfolio/portfolio.html', context)
