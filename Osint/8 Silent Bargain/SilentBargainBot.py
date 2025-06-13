from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN = "TOKEN_DELETED_SO_YOU_DON'T_MESS_UP_WITH_THE_BOT_SORRY!!"

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "Hello! I am your friendly bot. How can I help you today? Type /help for more options."
    )

async def help_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "Here are some commands you can use:\n"
        "/start - Start the bot\n"
        "/help - Display this help message\n"
        "/flag - Get the flag\n"
        "/joke - Hear a joke\n"
        "/info - Get some information\n"
    )

async def flag(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Walahi la te7chem -_- taw ena ye3lem baya l3ali kifeh ktebetha task wenta akeka toul dekhel /flag ? walahi la te7chem -_-")

async def joke(update: Update, context: CallbackContext) -> None:
    jokes = [
        "Why don’t skeletons fight each other? They don’t have the guts.",
        "I told my computer I needed a break, and now it won’t stop sending me Kit-Kats.",
        "Why don’t programmers like nature? It has too many bugs."
    ]
    await update.message.reply_text(jokes[0])

async def info(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "I am a simple Telegram bot created to interact with you. I can respond to commands like /flag, /joke, and more. Let's have some fun!"
    )

async def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text.lower()
    if "give me the flag, please" in user_message:
        await update.message.reply_text("Securinets{S1l3ntB4rg41n_HuntF0rD34ls}")
    elif "give me the flag please" in user_message:
        await update.message.reply_text("Securinets{S1l3ntB4rg41n_HuntF0rD34ls}")
    elif "give me the flag please." in user_message:
        await update.message.reply_text("Securinets{S1l3ntB4rg41n_HuntF0rD34ls}")
    else:
        await update.message.reply_text("I'm here to chat! Tell me something else or type /help for help")

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("flag", flag))
    application.add_handler(CommandHandler("joke", joke))
    application.add_handler(CommandHandler("info", info))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.run_polling()

if __name__ == "__main__":
    main()
