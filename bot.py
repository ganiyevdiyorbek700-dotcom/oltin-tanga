import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from keep_alive import keep_alive  # Render uchun uyg'otuvchi qism

# Sizning ma'lumotlaringiz
API_TOKEN = '8439775897' # Tokeningiz (Eslatma: BotFather bergan to'liq tokenni tekshiring)
WEBAPP_URL = 'https://ganiyevdiyorbek700-dotcom.github.io/Oltin-Tanga-/'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    args = message.get_args() 

    # Referal tizimi
    if args and args.isdigit() and int(args) != user_id:
        referrer_id = int(args)
        # Bu yerda Firebase-ga bonus yozish qismini keyinroq ulaymiz
        try:
            await bot.send_message(referrer_id, f"🎉 Tabriklaymiz! Do'stingiz qo'shildi. Sizga bonus tangalar berildi!")
        except:
            pass

    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("O'yinni boshlash 🎮", web_app=WebAppInfo(url=WEBAPP_URL)),
        InlineKeyboardButton("Do'stlarni taklif qilish 👥", callback_data="ref_link")
    )

    welcome_text = (
        f"<b>Assalomu alaykum, {message.from_user.first_name}!</b>\n\n"
        f"📀 Oltin Tanga o'yiniga xush kelibsiz!\n"
        f"Tanga bosing, ligalarda ko'tariling va do'stlaringiz bilan musobaqalashing."
    )
    
    await message.answer(welcome_text, reply_markup=markup)

@dp.callback_query_handler(text="ref_link")
async def share_link(call: types.CallbackQuery):
    user_id = call.from_user.id
    bot_info = await bot.get_me()
    ref_link = f"https://t.me/{bot_info.username}?start={user_id}"
    share_url = f"https://t.me/share/url?url={ref_link}&text=Do'stim, mana bu o'yinni ko'r! Birga tanga yig'amiz! 📀"
    
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Yuborish 🚀", url=share_url))
    
    await call.message.answer(f"Sizning taklif havolangiz:\n<code>{ref_link}</code>", reply_markup=markup)

if __name__ == '__main__':
    keep_alive() # Renderda uxlab qolmasligi uchun Flaskni yoqish
    executor.start_polling(dp, skip_updates=True)

