from .models import Order
from django.http import HttpResponse


def home_page(request):

    orders = Order.objects.all()
    text_for_print = []
    for o in orders:
        line = f'<h1>{o.number} - {o.price_dollars} - {o.delivery_time} - {o.price_rubles}<h1/>'
        text_for_print.append(line)
    return HttpResponse(text_for_print)

