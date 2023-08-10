from selenium import webdriver
from selenium.webdriver.common.by import By
import os

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