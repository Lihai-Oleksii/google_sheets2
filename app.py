from aiogram import executor

from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify

if __name__ == '__main__':
    executor.start_polling(dp)
