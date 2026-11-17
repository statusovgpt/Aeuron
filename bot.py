import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# Токен бота (получить у @BotFather)
BOT_TOKEN = os.getenv("BOT_TOKEN", "ВАШ_ТОКЕН_БОТА")

# Ссылка на страницу с игрой (вставьте свой URL)
WEBAPP_URL = os.getenv("WEBAPP_URL", "https://your-username.github.io/aureon-telegram-game/")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Баланс пользователей (хранится в памяти, сбрасывается при перезапуске)
user_balance = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_balance.setdefault(user_id, 1000)   # стартовый баланс

    keyboard = [[InlineKeyboardButton("🎮 Играть в Aureon",
                web_app=WebAppInfo(url=WEBAPP_URL))]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"👋 Привет, {update.effective_user.first_name}!\n"
        f"Твой баланс: {user_balance[user_id]} 🪙\n\n"
        "Нажми кнопку ниже, чтобы открыть веб‑игру.\n"
        "Валюта виртуальная, реальных денег нет.",
        reply_markup=reply_markup,
    )

async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bal = user_balance.get(update.effective_user.id, 0)
    await update.message.reply_text(f"💰 Твой баланс: {bal} 🪙")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("balance", balance))
    app.run_polling()

if __name__ == "__main__":
    main()
