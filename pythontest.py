
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
import os
from os import name
from selenium.webdriver.chrome.options import Options
from datetime import datetime,date
from dateutil.relativedelta import relativedelta
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(
    executable_path='C:/webdriver/chromedriver.exe')
driver.get("http://www.python.org")
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
time.sleep(3)
elem.send_keys(Keys.CONTROL + "a")
time.sleep(3)
elem.send_keys(Keys.CONTROL + "c")
time.sleep(3)
elem.send_keys("test")
time.sleep(3)

elem.send_keys(Keys.CONTROL + "a")
time.sleep(3)
elem.send_keys(Keys.CONTROL + "v")
time.sleep(3)