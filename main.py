import telebot
from telebot import types

# ⚠️ ВНИМАНИЕ: Для безопасности на GitHub токен скрыт!
# При запуске на компьютере вставьте ваш секретный ключ от @BotFather внутрь кавычек ниже.
TOKEN = 'ВАШ_СЕКРЕТНЫЙ_ТОКЕН_ИЗ_BOTFATHER'
bot = telebot.TeleBot(TOKEN)

# Главное меню бота
def get_main_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn_find = types.KeyboardButton("🔎 Find a thing")
    btn_categories = types.KeyboardButton("🛍 Categories")
    btn_about = types.KeyboardButton("ℹ️ About Clothyyy")
    keyboard.add(btn_find, btn_categories, btn_about)
    return keyboard

# Меню категорий
def get_categories_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn_clothing = types.KeyboardButton("👚 Clothing")
    btn_shoes = types.KeyboardButton("👟 Shoes")
    btn_bags = types.KeyboardButton("👜 Bags")
    btn_accessories = types.KeyboardButton("💍 Accessories")
    btn_back = types.KeyboardButton("⬅️ Back to Main Menu")
    keyboard.add(btn_clothing, btn_shoes, btn_bags, btn_accessories, btn_back)
    return keyboard

# Меню подкатегорий одежды
def get_clothing_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn_dresses = types.KeyboardButton("👗 Dresses")
    btn_tops = types.KeyboardButton("👕 Tops & T-shirts")
    btn_jeans = types.KeyboardButton("👖 Jeans & Trousers")
    btn_skirts = types.KeyboardButton("🩷 Skirts")
    btn_jackets = types.KeyboardButton("🧥 Jackets & Coats")
    btn_sweaters = types.KeyboardButton("🧶 Sweaters & Hoodies")
    btn_back = types.KeyboardButton("⬅️ Back to Categories")
    keyboard.add(btn_dresses, btn_tops, btn_jeans, btn_skirts, btn_jackets, btn_sweaters, btn_back)
    return keyboard

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "✦ **CLOTHYYY**\n"
        "_Find. Match. Shop._\n\n"
        "Find similar clothes and discover where you can buy them."
    )
    bot.send_message(message.chat.id, welcome_text, parse_mode='Markdown', reply_markup=get_main_keyboard())

# Обработка нажатий на кнопки
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "🔎 Find a thing":
        bot.send_message(message.chat.id, "📸 Пожалуйста, отправьте мне фотографию вещи, которую вы ищете!")
        
    elif message.text == "🛍 Categories":
        bot.send_message(message.chat.id, "Выберите интересующую вас категорию:", reply_markup=get_categories_keyboard())
        
    elif message.text == "ℹ️ About Clothyyy":
        about_text = (
            "✦ **Clothyyy** — это твой личный фэшн-помощник.\n\n"
            "Увидела классную вещь в Pinterest, но не знаешь, где её купить в Узбекистане? "
            "Просто отправь фото вещи боту, и мы найдем похожие варианты с ценами и ссылками на магазины, "
            "которые доставляют к нам!"
        )
        bot.send_message(message.chat.id, about_text, parse_mode='Markdown')

    elif message.text == "👚 Clothing":
        bot.send_message(message.chat.id, "Выберите тип одежды:", reply_markup=get_clothing_keyboard())
        
    elif message.text in ["👟 Shoes", "👜 Bags", "💍 Accessories"]:
        bot.send_message(message.chat.id, f"Вы выбрали раздел *{message.text}*. Совсем скоро здесь появятся трендовые подборки!", parse_mode='Markdown')
        
    elif message.text in ["👗 Dresses", "👕 Tops & T-shirts", "👖 Jeans & Trousers", "🩷 Skirts", "🧥 Jackets & Coats", "🧶 Sweaters & Hoodies"]:
        bot.send_message(message.chat.id, f"Вы заглянули в раздел *{message.text}*. Ищем лучшие предложения...", parse_mode='Markdown')

    elif message.text == "⬅️ Back to Categories":
        bot.send_message(message.chat.id, "Возвращаемся в категории:", reply_markup=get_categories_keyboard())
        
    elif message.text == "⬅️ Back to Main Menu":
        bot.send_message(message.chat.id, "Главное меню:", reply_markup=get_main_keyboard())

# Обработка отправки фото
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    bot.send_message(message.chat.id, "⏳ Идет сканирование образа... Ищем совпадения в магазинах Узбекистана.")

# Запуск бота
bot.infinity_polling()
