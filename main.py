import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from dotenv import load_dotenv
import os

load_dotenv()


# logger
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    """
    Sends a message on /start command
    """
    update.message.reply_text("Hi!")


def help_command(update, context):
    """
    Sends a message on /help command
    """
    update.message.reply_text("Help!")


def echo(update, context):
    """
    Echoes user's message
    """
    update.message.reply_text(update.message.text)


def main():
    """
    Start the bot
    """

    updater = Updater(
        os.getenv("TOKEN"), use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help_command))

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
