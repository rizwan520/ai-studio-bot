import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to AI STUDIO! ✨\n\n"
        "Choose your AI tool:\n"
        "🖼 AI Photo Editor\n"
        "💬 AI Chat\n"
        "🎨 Text to Image\n"
        "🎬 Video Face Swap\n"
        "🌟 Ready-made Scenes\n"
        "👤 AI Character"
    )

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("AI Chat is coming soon!")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

print("AI STUDIO is ready!")
app.run_polling()
