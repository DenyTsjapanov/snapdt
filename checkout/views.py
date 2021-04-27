from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing in your bag at the moment")
        return redirect(reverse('portfolio'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IkzQ6ErKlohyPQFF4rNl6yZOC6qv5Bp2r7GTw29oyIwxqyK9h5wi9FvLPG80dAJix2EPWdkUXtvoVtiBASRyYw100xebBc9VH',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)
