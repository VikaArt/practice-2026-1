from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

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
        "Я помогу тебе узнать о проекте, найти ресурсы и разобраться в рубриках.\n\n"
        "Выбери, что тебя интересует:",
        reply_markup=reply_markup
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "about":
        text = (
            "О проекте\n\n"
            "«Карта компетенций для выпускника» — навигатор, который помогает студентам "
            "развивать гибкие навыки и успешно трудоустраиваться.\n\n"
            "Цель: помочь студентам видеть свои сильные стороны и понимать, "
            "куда двигаться дальше — без воды и навязывания.\n\n"
            "Как работает:\n"
            "1. Диагностика — тестирование в Центрах компетенций РСВ\n"
            "2. Анализ — интерпретация результатов\n"
            "3. Рекомендации — персонализированные материалы\n"
            "4. Трудоустройство — паспорт компетенций в hh.ru"
        )

        await query.edit_message_text(text)

    elif query.data == "resources":
        keyboard = [
            [InlineKeyboardButton("Telegram-канал", url="https://t.me/probkartikompmospolitex")],
            [InlineKeyboardButton("ВК-сообщество", url="https://vk.com/club236925170")],
            [InlineKeyboardButton("Сайт проекта", url="https://profi-navigator.lovable.app/")],
            [InlineKeyboardButton("Назад", callback_data="back_to_menu")],
        ]

        await query.edit_message_text(
            "Наши ресурсы:\n\nВыбери, куда хочешь перейти:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "rubrics":
        text = (
            "Рубрики канала:\n\n"
            "#компетенция_просто — разбор навыка (2 раза в неделю)\n"
            "#инструкция_рсв — гайды по тестированию (1 раз в неделю)\n"
            "#карта_возможностей — стажировки и мероприятия\n"
            "#история_из_политеха — истории студентов\n"
            "#опрос_недели — опросы"
        )

        keyboard = [[InlineKeyboardButton("Назад", callback_data="back_to_menu")]]

        await query.edit_message_text(
            text,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "faq":
        text = (
            "Частые вопросы:\n\n"
            "Что такое РСВ?\n"
            "Платформа «Россия — страна возможностей».\n\n"
            "Где пройти тест?\n"
            "В Центре компетенций Московского Политеха.\n\n"
            "Как попасть в канал?\n"
            "Через меню «Наши ресурсы».\n\n"
            "Что делать, если не знаю компетенцию?\n"
            "Напиши нам — поможем разобраться!"
        )

        keyboard = [[InlineKeyboardButton("Назад", callback_data="back_to_menu")]]

        await query.edit_message_text(
            text,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "back_to_menu":
        keyboard = [
            [InlineKeyboardButton("О проекте", callback_data="about")],
            [InlineKeyboardButton("Наши ресурсы", callback_data="resources")],
            [InlineKeyboardButton("Рубрики канала", callback_data="rubrics")],
            [InlineKeyboardButton("Частые вопросы", callback_data="faq")],
        ]

        await query.edit_message_text(
            "Главное меню:\n\nВыбери, что тебя интересует:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Бот запущен...")
    app.run_polling()


if __name__ == "__main__":
    main()
