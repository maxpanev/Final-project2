from telegram import Bot
from django.conf import settings
from .models import Order

def send_order_to_telegram(order: Order):
    bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
    message = (
        f"Новый заказ!\n"
        f"Пользователь: {order.user.username}\n"
        f"Товары: {', '.join(f'{item.product.name} (x{item.quantity})' for item in order.basket.items.all())}\n"
        f"Стоимость: {sum(item.product.price * item.quantity for item in order.basket.items.all())}\n"
        f"Дата доставки: {order.date}\n"
        f"Время доставки: {order.time}\n"
        f"Адрес доставки: {order.city}, {order.address}\n"
    )
    bot.send_message(chat_id=settings.TELEGRAM_CHAT_ID, text=message)