import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from flask import Flask
from threading import Thread

# Sozlamalar
API_TOKEN = '8439775897' 
WEBAPP_URL = 'https://ganiyevdiyorbek700-dotcom.github.io/Oltin-Tanga-/'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN, parse_mode="HTML")
dp = Dispatcher()

# Flask (Render uchun)
app = Flask('')
@app.route('/')
def home(): return "Bot Live!"

def run(): app.run(host='0.0.0.0', port=8080)

@dp.message(commands=['start'])
async def cmd_start(message: types.Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="O'yinni boshlash 🎮", web_app=WebAppInfo(url=WEBAPP_URL))],
        [InlineKeyboardButton(text="Do'stlarni taklif qilish 👥", callback_data="ref")]
    ])
    await message.answer(f"Salom {message.from_user.first_name}! Tanga yig'ishni boshlang!", reply_markup=markup)

async def main():
    Thread(target=run).start()
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
    

