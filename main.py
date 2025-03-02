Создание Telegram-бота на Python с использованием библиотеки `python-telegram-bot` версии 20.x, который показывает случайные факты о птицах, включает в себя несколько шагов. Мы также добавим обработку ошибок и логирование.

### Шаг 1: Установка необходимых библиотек

Для начала установим необходимые библиотеки:

```bash
pip install python-telegram-bot
```

### Шаг 2: Создание бота

Создадим файл `bird_facts_bot.py` и начнем писать код.

```python
import logging
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Список случайных фактов о птицах
BIRD_FACTS = [
    "Страусы могут бегать быстрее лошадей.",
    "Пингвины могут прыгать в высоту до 2 метров.",
    "Колибри — единственные птицы, которые могут летать назад.",
    "У совы три века: одно для моргания, одно для сна и одно для защиты глаз.",
    "Попугаи могут жить более 80 лет.",
    "Альбатросы могут спать во время полета.",
    "Вороны могут узнавать себя в зеркале.",
    "Фламинго розовые из-за своего рациона, который состоит из креветок и водорослей.",
    "Киви — единственная птица, у которой ноздри находятся на кончике клюва.",
    "Птицы-секретари известны своей способностью охотиться на змей."
]

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот, который рассказывает случайные факты о птицах. Используй команду /fact, чтобы узнать что-то новое.")

# Команда /fact
async def fact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        fact = random.choice(BIRD_FACTS)
        await update.message.reply_text(fact)
    except Exception as e:
        logger.error(f"Ошибка при получении факта: {e}")
        await update.message.reply_text("Произошла ошибка при получении факта. Попробуйте еще раз.")

# Обработка ошибок
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f"Ошибка: {context.error}")
    await update.message.reply_text("Произошла ошибка. Пожалуйста, попробуйте еще раз.")

# Основная функция
def main():
    # Создаем приложение и передаем токен бота
    application = ApplicationBuilder().token("YOUR_TELEGRAM_BOT_TOKEN").build()

    # Регистрируем обработчики команд
    start_handler = CommandHandler('start', start)
    fact_handler = CommandHandler('fact', fact)

    application.add_handler(start_handler)
    application.add_handler(fact_handler)

    # Регистрируем обработчик ошибок
    application.add_error_handler(error_handler)

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
```

### Шаг 3: Запуск бота

1. Замените `"YOUR_TELEGRAM_BOT_TOKEN"` на токен вашего бота, который вы получили от BotFather.
2. Запустите скрипт:

```bash
python bird_facts_bot.py
```

### Шаг 4: Использование бота

Теперь вы можете взаимодействовать с ботом в Telegram:

- Используйте команду `/start`, чтобы начать взаимодействие с ботом.
- Используйте команду `/fact`, чтобы получить случайный факт о птицах.

### Шаг 5: Логирование и обработка ошибок

Логирование настроено так, чтобы записывать все ошибки и информацию о работе бота в консоль. Если произойдет ошибка, бот сообщит об этом пользователю и попросит попробовать еще раз.

### Заключение

Теперь у вас есть полнофункциональный Telegram-бот, который может показывать случайные факты о птицах. Вы можете расширить функциональность бота, добавив больше команд или улучшив обработку ошибок и логирование.