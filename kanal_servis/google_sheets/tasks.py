import os
from kanal_servis.celery import app
from datetime import datetime
from telegram import Bot

from .service import get_google_sheets_data, get_dollar_price
from .models import Order

from dotenv import load_dotenv

load_dotenv()


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
    my_orders = Order.objects.all()
    for order in my_orders:
        if str(order.number) not in number:
            order.delete()


@app.task
def new_price():
    """Функция обновляет цену заказа в соответствии с актуальным курсом валют ЦБ"""
    my_orders = Order.objects.all()
    price = get_dollar_price()

    for order in my_orders:
        order.price_rubles = order.price_dollars * price
        order.save()


@app.task
def delivery_time_bot():
    """Telegram bot отправляет сообщения пользователю если настал день доставки"""
    bot = Bot(token=os.getenv('TOKEN'))
    chat_id = os.getenv('CHAT_ID')
    my_orders = Order.objects.all()
    today = datetime.today().date()
    for order in my_orders:
        if order.delivery_time == today:
            text = f'Заказ №{order.number} будет доставлен сегодня'
            bot.send_message(chat_id, text)
