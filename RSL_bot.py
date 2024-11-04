from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Список героев и ссылки на их описания
heroes_data = {
    "Каэль": "https://telegra.ph/Kaehl-11-04",
    "Элейн": "https://telegra.ph/Elhain-Raid-Shadow-Legends-09-01",
    "Галек": "https://telegra.ph/Galek-Raid-Shadow-Legends-09-01",
    "Этель": "https://telegra.ph/Athel-Raid-Shadow-Legends-09-01"
    # Добавьте больше героев и их ссылки здесь
}

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [[InlineKeyboardButton("Герои", callback_data="show_heroes")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Добро пожаловать! Нажмите кнопку ниже, чтобы увидеть список героев.", reply_markup=reply_markup)

# Обработчик кнопки героев
async def show_heroes(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    # Создание кнопок для каждого героя
    keyboard = [[InlineKeyboardButton(hero, callback_data=hero)] for hero in heroes_data]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text("Выберите героя:", reply_markup=reply_markup)

# Обработчик выбора героя
async def hero_info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    hero_name = query.data
    hero_url = heroes_data.get(hero_name, "Информация недоступна")

    await query.edit_message_text(f"Описание для {hero_name}: [Сборки и применения]({hero_url})", parse_mode="Markdown")

# Основная функция для запуска бота
def main():
    # Вставьте свой токен ниже
    application = Application.builder().token("7666510134:AAFubFwg_SR4VTgzil6pJXM2sWhMrWolOPY").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(show_heroes, pattern="^show_heroes$"))
    application.add_handler(CallbackQueryHandler(hero_info))

    application.run_polling()

if __name__ == "__main__":
    main()


