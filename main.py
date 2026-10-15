import telebot
from telebot import types

# ⚠️ ВНИМАНИЕ: Для безопасности на GitHub настоящий токен скрыт!
# При запуске бота на компьютере вставьте ваш рабочий ключ от @BotFather внутрь кавычек ниже.
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

# Меню категорий каталога
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

# Приветственное меню при вводе команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "✦ **CLOTHYYY**\n"
        "_Find. Match. Shop._\n\n"
        "Привет! Добро пожаловать в fashion-помощник clothyyv.\n"
        "Здесь ты можешь легко найти похожую одежду и узнать, где её выгодно заказать с быстрой доставкой в Узбекистан!"
    )
    bot.send_message(message.chat.id, welcome_text, parse_mode='Markdown', reply_markup=get_main_keyboard())

# Обработка интерактивных текстовых кнопок меню
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "🔎 Find a thing":
        bot.send_message(message.chat.id, "📸 Пожалуйста, отправь мне фотографию вещи из Pinterest, а я попробую отыскать её аналоги!")
        
    elif message.text == "🛍 Categories":
        bot.send_message(message.chat.id, "Выбери категорию, которая тебя интересует в каталоге:", reply_markup=get_categories_keyboard())
        
    elif message.text == "ℹ️ About Clothyyy":
        about_text = (
            "✦ **Clothyyy** — твой персональный стилист-навигатор.\n\n"
            "Увидела потрясающий образ в интернете, но понятия не имеешь, где купить его в Узбекистане? "
            "Просто выбери нужную категорию одежды или отправь фото вещи нашему боту. "
            "Мы моментально подберем похожие трендовые варианты с актуальными ценами в сумах и прямыми ссылками на маркетплейсы Uzum и Ozon!"
        )
        bot.send_message(message.chat.id, about_text, parse_mode='Markdown')

    elif message.text == "👚 Clothing":
        bot.send_message(message.chat.id, "Выбери тип одежды, который ты ищешь:", reply_markup=get_clothing_keyboard())

    # =========================================================================
    #             ПОЛНАЯ КУРИРОВАННАЯ БАЗА ССЫЛОК ОТ ОБЕИХ УЧЕНИЦ
    # =========================================================================

    elif message.text == "👕 Tops & T-shirts":
        try:
            with open('longsleeve.jpg', 'rb') as photo:
                text = (
                    "👕 **Зелёный лонгслив в полоску**\n\n"
                    "🛍 *Uzum Вариант 1:* Женский хлопковый базовый лонгслив\n"
                    "🔗 [Купить на Uzum Market](https://uzum.uz)\n"
                    "🛍 *Uzum Вариант 2:* Оверсайз футболка с длинным рукавом\n"
                    "🔗 [Купить на Uzum Market](https://uzum.uz)\n"
                    "🛍 *Ozon Вариант 3:* Полосатый хлопковый лонгслив\n"
                    "🔗 [Купить на Ozon](https://ozon.uz)\n\n"
                    "-----------------------------------\n"
                    "👕 **Новинки от Софии: Трендовые футболки и блузы**\n"
                    "🛍 *Ozon Полосатая блуза:* Приталенная рубашка ANGELS ASYLUM\n"
                    "🔗 [Купить на Ozon](https://ozon.uz/t/yebSYFB)\n"
                    "🛍 *Ozon Повседневная:* Рубашка Befree с коротким рукавом в клетку\n"
                    "💰 Цена: 301 481 сум\n"
                    "🔗 [Купить на Ozon](https://ozon.uz/t/1fnyHM0)\n"
                    "🛍 *Ozon Мультяшная:* Футболка с принтом Paul Frank (худи с обезьянкой)\n"
                    "💰 Цена: 208 986 сум\n"
                    "🔗 [Купить на Ozon](https://ozon.uz/t/9oLUZEo)"
                )
                bot.send_photo(message.chat.id, photo, caption=text, parse_mode='Markdown')
        except FileNotFoundError:
            bot.send_message(message.chat.id, "⚠️ Ошибка: Файл 'longsleeve.jpg' не найден в папке бота!")

    elif message.text == "👖 Jeans & Trousers":
        try:
            with open('pants.jpg', 'rb') as photo:
                text = (
                    "👖 **Широкие серые спортивные штаны с лампасами**\n\n"
                    "🛍 *Uzum Вариант 1:* Свободные серыы штаны-джоггеры\n"
                    "🔗 [Купить на Uzum Market](https://uzum.uz)\n"
                    "🛍 *Uzum Вариант 2:* Повседневные оверсайз Baggy Y2K джоггеры\n"
                    "🔗 [Купить на Uzum Market](https://uzum.uz)\n"
                    "🛍 *Ozon Вариант 3:* Серые спортивные брюки свободного кроя\n"
                    "🔗 [Купить на Ozon](https://ozon.uz)"
                )
                bot.send_photo(message.chat.id, photo, caption=text, parse_mode='Markdown')
        except FileNotFoundError:
            bot.send_message(message.chat.id, "⚠️ Ошибка: Файл 'pants.jpg' не найден в папке бота!")

    elif message.text == "👗 Dresses":
        try:
            with open('dress.jpg', 'rb') as photo:
                text = (
                    "👗 **Нежное розовое платье с клубничками и воротником**\n\n"
                    "🛍 *Uzum Вариант 1:* Хлопковое платье весна-лето с принтом\n"
                    "🔗 [Купить на Uzum Market](https://uzum.uz)\n"
                    "🛍 *Uzum Вариант 2:* Нарядное хлопковое платье с отложным воротником\n"
                    "🔗 [Купить на Uzum Market](https://uzum.uz)\n\n"
                    "-----------------------------------\n"
                    "🛍 *Софиюша Выбор:* Нарядное платье для девочек в нежном стиле\n"
                    "🔗 [Купить на Ozon](https://ozon.uz/t/OyxBIBk)"
                )
                bot.send_photo(message.chat.id, photo, caption=text, parse_mode='Markdown')
        except FileNotFoundError:
            bot.send_message(message.chat.id, "⚠️ Ошибка: Файл 'dress.jpg' не найден в папке бота!")

    elif message.text == "🧥 Jackets & Coats":
        try:
            with open('coat.jpg', 'rb') as photo:
                text = (
                    "🧥 **Серое шерстяное пальто и приталенный жакет**\n\n"
                    "🛍 *Uzum Вариант 1:* Короткое демисезонное пальто оверсайз с поясом\n"
                    "🔗 [Купить на Uzum Market](https://uzum.uz)\n"
                    "🛍 *Uzum Вариант 2:* Женское укороченное пальто с воротником-стойкой\n"
                    "🔗 [Купить на Uzum Market](https://uzum.uz)\n\n"
                    "-----------------------------------\n"
                    "🧥 **Новинки от Софии: Пиджаки и верхняя одежда**\n"
                    "🛍 *Ozon Школьный:* Темно-синий хлопковый пиджак FAY для девочек\n"
                    "💰 Цена: 445 610 сум\n"
                    "🔗 [Купить на Ozon](https://ozon.uz/t/l1MOaPp)\n"
                    "🛍 *Ozon Альтернатива:* Элегантный укороченный блейзер\n"
                    "🔗 [Купить на Ozon](https://ozon.uz/t/7G4M4F9)"
                )
                bot.send_photo(message.chat.id, photo, caption=text, parse_mode='Markdown')
        except FileNotFoundError:
            bot.send_message(message.chat.id, "⚠️ Ошибка: Файл 'coat.jpg' не найден в папке бота!")

    elif message.text == "🧶 Sweaters & Hoodies":
        try:
            with open('cardigan.jpg', 'rb') as photo:
                text = (
                    "🧶 **Серый вязаный кардиган и теплые кофты**\n\n"
                    "🛍 *Uzum Вариант 1:* Женский вязаный кардиган на пуговицах\n"
                    "🔗 [Купить на Uzum Market](https://uzum.uz)\n"
                    "🛍 *Uzum Вариант 2:* Однотонный лонгслив на пуговицах с длинным рукавом\n"
                    "🔗 [Купить на Uzum Market](https://uzum.uz)\n"
                    "🛍 *Ozon Вариант 3:* Мягкий укороченный кардиган корейского стиля\n"
                    "🔗 [Купить на Ozon](https://ozon.uz)\n\n"
                    "-----------------------------------\n"
                    "🧶 **Новинки от Софии: Стильные худи и свитшоты**\n"
                    "🛍 *Ozon Уличный стиль:* Толстовка Befree на молнии в полоску с капюшоном\n"
                    "💰 Цена: 460 513 сум\n"
                    "🔗 [Купить на Ozon](https://ozon.uz/t/qtXFjc8)\n"
                    "🛍 *Ozon Базовый:* Мужской/Унисекс серый меланж свитшот без начеса\n"
                    "💰 Цена: 296 476 сум\n"
                    "🔗 [Купить на Ozon](https://ozon.uz/t/OyxBhFW)\n"
