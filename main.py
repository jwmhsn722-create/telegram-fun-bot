import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = "8208673472:AAFiuQU-w8eUPOurs88lOEWDPRQCSlqnohw"
ADMIN_ID = 7938265558  # آیدی عددی خودت

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton("👩 دخترم", callback_data="girl"),
        InlineKeyboardButton("👨 پسرم", callback_data="boy")
    )
    bot.send_message(
        message.chat.id,
        "سلام 😄\nاول بگو دختر هستی یا پسر؟",
        reply_markup=keyboard
    )

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "girl":
        bot.send_message(
            call.message.chat.id,
            "🌸 خوش اومدی!\nالان وصل شدی به ادمین 😉"
        )
        bot.send_message(
            ADMIN_ID,
            f"👩 یک دختر وارد ربات شد!\nآیدی: @{call.from_user.username}"
        )

    elif call.data == "boy":
        bot.send_message(
            call.message.chat.id,
            "😂 پسر جان برو درس‌تو بخون!\nفعلاً خدافظ!"
        )

bot.polling()
