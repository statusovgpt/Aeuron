# Aureon Telegram Game

Telegram-бот с встроенной веб-игрой и виртуальной экономикой без реальных денег.

## Структура

- `bot.py` — Telegram-бот (python-telegram-bot)
- `index.html` — веб-игра (Telegram Web App)
- `requirements.txt` — зависимости
- `.gitignore` — игнорируемые файлы

## Быстрый старт

1. Создай бота через [@BotFather](https://t.me/BotFather) и получи токен.
2. В `bot.py` замени `ВАШ_ТОКЕН_БОТА` на свой токен.
3. Загрузи `index.html` на любой хостинг (GitHub Pages, Vercel, Netlify и т.д.).
4. В `bot.py` замени `WEBAPP_URL` на ссылку на свою веб-игру.
5. Установи зависимости:

```bash
pip install -r requirements.txt
