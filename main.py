import telebot

# Замените ТОКЕН внутри кавычек на ваш секретный ключ от @BotFather
TOKEN = ' 8820568834:AAFboucjaAMK52bPph3acetYcxO3Jkyd0Js '
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "привет! это наш школьный бот по поиску одежды clothyyv. скоро мы настроим здесь поиск по фото!")

# Запуск бота
bot.infinity_polling()
