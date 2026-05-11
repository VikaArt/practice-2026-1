from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler

TOKEN = "8711109416:AAHEsO2Bf-tvtoP7Escs09h1n0nRdNiuSWw"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("О проекте", callback_data="about")],
        [InlineKeyboardButton("Наши ресурсы", callback_data="resources")],
        [InlineKeyboardButton("Рубрики канала", callback_data="rubrics")],
        [InlineKeyboardButton("Частые вопросы", callback_data="faq")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Привет! Я бот-навигатор проекта «Карта компетенций для выпускника».\n\n"
        "Я помогу тебе узнать о проекте, найти все наши ресурсы и разобраться в рубриках.\n\n"
        "Выбери, что тебя интересует:",
        reply_markup=reply_markup
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "about":
        text = (
            "**О проекте**\n\n"
            "«Карта компетенций для выпускника» — это навигатор, который помогает студентам "
            "Московского Политеха развивать гибкие навыки и успешно трудоустраиваться.\n\n"
            "**Цель:** помочь студентам видеть свои сильные стороны и понимать, "
            "куда двигаться дальше — без воды и навязывания.\n\n"
            "**Как работает:**\n"
            "1. Диагностика — тестирование в Центрах компетенций РСВ\n"
            "2. Анализ — интерпретация результатов\n"
            "3. Рекомендации — персонализированные материалы\n"
            "4. Трудоустройство — паспорт компетенций в hh.ru"
        )
        await query.edit_message_text(text, parse_mode="Markdown")

    elif query.data == "resources":
        keyboard = [
            [InlineKeyboardButton("Telegram-канал", url="https://t.me/probkartikompmospolitex")],
            [InlineKeyboardButton("ВК-сообщество", url="https://vk.com/club236925170")],
            [InlineKeyboardButton("Сайт проекта", url="https://profi-navigator.lovable.app/")],
            [InlineKeyboardButton("Назад", callback_data="back_to_menu")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "**Наши ресурсы**\n\nВыбери, куда хочешь перейти:",
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )

    elif query.data == "rubrics":
        text = (
            "**Рубрики канала**\n\n"
            "**#компетенция_просто** — короткий разбор навыка. 2 раза в неделю\n\n"
            "**#инструкция_рсв** — пошаговые гайды по тестированию. 1 раз в неделю\n\n"
            "**#карта_возможностей** — подборка стажировок и мероприятий. 1 раз в неделю\n\n"
            "**#история_из_политеха** — реальные истории студентов. 2 раза в месяц\n\n"
            "**#опрос_недели** — вовлекающие опросы. 1 раз в неделю"
        )
        keyboard = [[InlineKeyboardButton("Назад", callback_data="back_to_menu")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

    elif query.data == "faq":
        text = (
            "**Частые вопросы**\n\n"
            "**Что такое РСВ?**\n"
            "РСВ — платформа «Россия – страна возможностей», где можно пройти диагностику компетенций.\n\n"
            "**Где пройти тест?**\n"
            "В Центре компетенций Московского Политеха.\n\n"
            "**Как попасть в Telegram-канал?**\n"
            "Нажми «Наши ресурсы» в меню → выбери Telegram-канал.\n\n"
            "**Что делать, если не знаю, какую компетенцию развивать?**\n"
            "Напиши нам в Telegram-канал — поможем разобраться!"
        )
        keyboard = [[InlineKeyboardButton("Назад", callback_data="back_to_menu")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")

    elif query.data == "back_to_menu":
        keyboard = [
            [InlineKeyboardButton("О проекте", callback_data="about")],
            [InlineKeyboardButton("Наши ресурсы", callback_data="resources")],
            [InlineKeyboardButton("Рубрики канала", callback_data="rubrics")],
            [InlineKeyboardButton("Частые вопросы", callback_data="faq")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "Главное меню\n\nВыбери, что тебя интересует:",
            reply_markup=reply_markup
        )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
