from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

################## Set up browser ##################
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")  
try:
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
except:
    driver = webdriver.Chrome(options=chrome_options)

driver.get('https://medium.com/geekculture/2-easy-ways-to-read-google-sheets-data-using-python-9e7ef366c775')
header = driver.find_element(By.TAG_NAME,'h1').text
print(header)


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
    bot_message = 'AWS EC2 Running'
    telegram_bot_sendtext(bot_message, BOT_TOKEN, chat_id,'')
    time.sleep(120)