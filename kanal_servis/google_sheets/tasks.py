from kanal_servis.celery import app
from datetime import datetime

from .service import get_google_sheets_data, get_dollar_price
from .models import Order


@app.task
def order_create():
    """Функция обновляет бд в соответствии с таблицей google sheets"""
    google_sheets_data = get_google_sheets_data()['values']
    number = google_sheets_data[0]
    price_dollars = google_sheets_data[1]
    delivery_time = google_sheets_data[2]
    price_cb = get_dollar_price()
    for i in range(len(number)):
        price_rubles = price_cb * float(price_dollars[i])

        Order.objects.update_or_create(
            number=int(number[i]),
            defaults={
                'price_dollars': float(price_dollars[i]),
                'delivery_time': datetime.strptime(delivery_time[i], "%d.%m.%Y"),
                'price_rubles': price_rubles
            },
        )


@app.task
def new_price():
    """Функция обновляет цену заказа в соответствии с актуальным курсом валют ЦБ"""
    my_orders = Order.objects.all()
    price = get_dollar_price()

    for order in my_orders:
        order.price_rubles = order.price_dollars * price
        order.save()
