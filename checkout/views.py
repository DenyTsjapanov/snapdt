from django.shortcuts import render, redirect, reverse
from django.contrib import mesaages

from .forms import OrderForm


def checkout(reqeust):
    bag = request.session.get('bag', {})
    if not bag:
        message.error(request, "There is nothing in your bag at the moment")
        return redirect(reverse('portfolio'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request. template, context)
