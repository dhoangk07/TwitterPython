import requests
import config

def send_to_telegram(message):
  apiURL = f'https://api.telegram.org/bot{config.TELEGRAM_BOT_TOKEN}/sendMessage'

  try:
    response = requests.post(apiURL, json={'chat_id': config.TELEGRAM_CHAT_ID, 'text': message})
    print(response.text)
  except Exception as e:
    print(e)

def send_error_to_telegram(message):
  apiURL = f'https://api.telegram.org/bot{config.TELEGRAM_BOT_TOKEN}/sendMessage'

  try:
    response = requests.post(apiURL, json={'chat_id': config.TELEGRAM_ERROR_CHANNEL, 'text': message})
    print(response.text)
  except Exception as e:
    print(e)
