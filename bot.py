import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo
from aiogram.filters import Command
import logging

# Токен бота (замени на свой)
TOKEN = "7644991979:AAGEjqyOf85SYo6S_g6mN_BfKf1gnCMQuUk"

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# URL веб-приложения (замени на свой)
WEB_APP_URL = "t.me/vilsonhotelbot/vilsonaiassistant"  # Ссылка на мини-приложение


# Обработчик команды /start
@dp.message(Command("start"))
async def start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    web_app_button = types.KeyboardButton(
        text="🔗 Відкрити асистента",
        web_app=WebAppInfo(url=WEB_APP_URL)
    )
    keyboard.add(web_app_button)

    await message.answer(
        "👋 Вітаємо! Натисніть кнопку нижче, щоб відкрити асистента Vilson!",
        reply_markup=keyboard
    )


# Запуск бота
async def main():
    logging.basicConfig(level=logging.INFO)
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

