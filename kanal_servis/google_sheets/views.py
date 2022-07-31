from .models import Order
from django.shortcuts import render


def home_page(request):
    template = 'home.html'
    orders = Order.objects.all()
    context = {
        'orders': orders
    }
    return render(request, template, context)

