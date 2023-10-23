python
import telebot
from googletrans import Translator

# توکن ربات تلگرام خود را در این قسمت وارد کنید
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

bot = telebot.TeleBot(TOKEN)
translator = Translator(service_urls=['translate.google.com'])

@bot.message_handler(func=lambda message: True)
def translate_message(message):
text = message.text

# تشخیص زبان متن و تعیین زبان مقصد براساس نوع زبان ورودی
if translator.detect(text).lang == 'fa':
dest_lang = 'en'
else:
dest_lang = 'fa'

# ترجمه متن با استفاده از گوگل ترنسلیت
translated_text = translator.translate(text, dest=dest_lang).text

# ارسال پاسخ به کاربر
bot.reply_to(message, translated_text)

bot.polling()