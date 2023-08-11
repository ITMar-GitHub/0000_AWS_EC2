from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import requests
# Telegram bot message function
def telegram_bot_sendtext(bot_message, token, chat_id, topic):
    
    bot_token = token
    bot_chatID = chat_id
    
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&message_thread_id=' + topic + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

while True:
    # Variables 
    chat_id='-949260927'
    BOT_TOKEN = '5916112518:AAHa5nPZtsMYdvxt-Ow5Z5gq-T6TMnWD1Fw'
    bot_message = 'AWS EC2 Oddspedia Running'
    telegram_bot_sendtext(bot_message, BOT_TOKEN, chat_id,'')
    time.sleep(3600)