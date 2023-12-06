# Cryptocurrency Rate Telegram Bot

This Telegram bot checks the cryptocurrency rate and sends notifications on rate changes.

## Prerequisites

- [Python](https://www.python.org/) installed
- Install required packages:
  ```bash
  pip install python-telegram-bot
  pip install requests
  ```
## Configuration
Obtain a Telegram bot token from @BotFather.  
Replace 'YOUR_TELEGRAM_BOT_TOKEN' with the obtained token.  
Obtain a cryptocurrency API key for rate tracking.  
Replace 'YOUR_CRYPTO_API_KEY' with the obtained API key.  

## Usage
Start the bot by running the script:

```bash
python crypto_bot.py
```

Open your Telegram client and find the bot by its username.

Use the following commands:

  - /start: Start the bot and receive a welcome message.
  - /check_rate: Check the cryptocurrency rate and receive a notification if it has changed.

## Notes
  - This script uses the python-telegram-bot library for interacting with the Telegram API.
  - The requests library is used for making HTTP requests to the cryptocurrency API.

## Disclaimer
This is a basic example script and may require additional features and error handling for a production environment.
