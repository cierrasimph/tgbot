import os
import requests
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Set your Telegram bot token
TELEGRAM_BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
# Set the API key and cryptocurrency symbol
CRYPTO_API_KEY = 'YOUR_CRYPTO_API_KEY'
CRYPTO_SYMBOL = 'BTC'

# Global variable to store the previous rate value
previous_rate = None

def start(update: Update, context: CallbackContext) -> None:
     update.message.reply_text('Hi! I'm a bot for tracking cryptocurrency rates.')

def check_crypto_rate(update: Update, context: CallbackContext) -> None:
     global previous_rate

     # Get the current cryptocurrency rate
     current_rate = get_crypto_currency_rate()

     # Check if the exchange rate has changed
     if is_rate_changed(current_rate):
         # Send a notification to Telegram
         update.message.reply_text(f'The cryptocurrency rate {CRYPTO_SYMBOL} has changed. New rate: {current_rate}')

     # Update the previous rate value
     previous_rate = current_rate

def get_crypto_currency_rate() -> float:
     # Simulate an API request (replace this block of code with a real API request)
     # In a real project, it is recommended to use a library for working with HTTP requests, such as requests.

     # Return a random value for example
     return round((10000 + os.urandom(1)[0]) / 100, 2) # Replace this line with the actual code for getting the rate

def is_rate_changed(current_rate: float) -> bool:
     global previous_rate

     # In this example, we consider that the rate has changed if it has decreased by 1%
     # In a real project, the verification logic may be more complex.

     return (previous_rate is None) or (current_rate < 0.99 * previous_rate) or (current_rate > 1.01 * previous_rate)

def main() -> None:
     # Initialization of the Telegram bot
     updater = Updater(TELEGRAM_BOT_TOKEN)
     dispatcher = updater.dispatcher

     # Adding command handlers
     dispatcher.add_handler(CommandHandler("start", start))
     dispatcher.add_handler(CommandHandler("check_rate", check_crypto_rate))

     # Launching a Telegram bot
     updater.start_polling()
     updater.idle()

if __name__ == '__main__':
     main()
