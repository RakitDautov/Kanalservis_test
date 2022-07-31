import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kanal_servis.settings")

app = Celery("kanal_servis")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

# Запускает task обновление базы Order раз в минуту
# обновление цены доллара каждый день в 10
# телеграм бота, отслеживающего доставку, каждый день в 10
app.conf.beat_schedule = {
    "update_order": {
        "task": "google_sheets.tasks.order_create",
        "schedule": crontab(),
    },
    "update_price": {
        "task": "google_sheets.tasks.new_price",
        "schedule": crontab(hour=10),
    },
    "telegram_bot": {
        "task": "google_sheets.tasks.delivery_time_bot",
        "schedule": crontab(hour=10),
    },
}
