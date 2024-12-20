import requests
from django.conf import settings
from .models import Order

def send_order_to_telegram(order: Order):
    message = (
        f"Новый заказ!\n"
        f"Клиент: {order.user.username}\n"
        f"Товары: {', '.join(f'{item.product.name} (x{item.quantity})' for item in order.items.all())}\n"
        f"Стоимость: {sum(item.product.price * item.quantity for item in order.items.all())}\n"
        f"Дата доставки: {order.date}\n"
        f"Время доставки: {order.time}\n"
        f"Адрес доставки: {order.city}, {order.address}\n"
        f"Телефон клиента: {order.phone}\n"  # Новая строка для отображения телефона
        f"Комментарий: {order.comment if order.comment else 'Нет'}\n"  # Добавляем комментарий
    )

    url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": settings.TELEGRAM_CHAT_ID,
        "text": message
    }

    response = requests.post(url, data=data)
    if response.status_code != 200:
        # Обработка ошибки
        print("Ошибка при отправке сообщения в Telegram:", response.text)