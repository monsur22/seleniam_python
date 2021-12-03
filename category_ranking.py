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
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--window-size=1920x1080')
options.add_argument('--headless')
path = os.path.dirname(os.path.abspath(__file__))
print(path)
print(os.getcwd() + os.path.sep)
options.add_experimental_option("prefs", {
"download.default_directory": os.getcwd() + os.path.sep,
"download.prompt_for_download": False,
"download.directory_upgrade": True,
"safebrowsing_for_trusted_sources_enabled": False,
"safebrowsing.enabled": False
})
driver = webdriver.Chrome(
    executable_path='C:/webdriver/chromedriver.exe')
# driver = webdriver.Chrome('C:/webdriver/chromedriver.exe', options=options)


driver.get("https://glogin.rms.rakuten.co.jp/?sp_id=1")
# identify username, password and signin elements
# first login
driver.find_element_by_name("login_id").send_keys("")
time.sleep(0.2)
driver.find_element_by_name("passwd").send_keys("")
time.sleep(0.4)
driver.find_element_by_class_name("rf-button-primary").click()
driver.close
# second login
driver.find_element_by_name("user_id").send_keys("")
time.sleep(0.2)
driver.find_element_by_name("user_passwd").send_keys("")
time.sleep(0.4)
driver.find_element_by_class_name("rf-button-primary").click()
driver.close
driver.find_element_by_class_name("rf-button-primary").click()
time.sleep(0.4)

# -------------------------------------now hit any url--------------------------------------------

# driver.find_element_by_class_name("btn-reset").click()

# driver.get("https://ad.rms.rakuten.co.jp/cpnadv/download_history")

driver.find_element_by_class_name("btn-reset").click()
driver.get("https://datatool.rms.rakuten.co.jp/access/category")
driver.find_element_by_xpath('//*[@id="root"]/div/main/div[1]/div/div[3]/div[1]/div/div/div[2]/div[2]/div[1]/div/label/span[2]').click()
time.sleep(5)
# driver.find_element_by_xpath('//*[@id="root"]/div/main/div[1]/div/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div/input').click()
element = driver.find_element_by_xpath('//*[@id="root"]/div/main/div[1]/div/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div/input')
time.sleep(3)
driver.execute_script("arguments[0].removeAttribute('readonly','readonly')",element) #remove the readonly attribute
print("remove attribute readonly")
d = "2021/10 - 2021/10"
print(d)
search = driver.find_element_by_xpath('//*[@id="root"]/div/main/div[1]/div/div[3]/div[2]/div/div/div[2]/div/input')
search.click()

print("click search field")
search.send_keys(d)
print("send keys date")
print("input search field")
time.sleep(3)
search.send_keys(Keys.CONTROL + "a")
time.sleep(3)
search.send_keys(Keys.CONTROL + "x")
time.sleep(3)

element.send_keys(Keys.CONTROL + "a")
element.send_keys(Keys.DELETE)
element.send_keys(Keys.CONTROL + "v")

driver.find_element_by_xpath('/html/body/div[3]/div[4]/button[2]').click()

# element.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE, Keys.CONTROL + 'v')
# element.send_keys(d)

# end_date = "2021/10"
# end_date = end_date[0:7]
# end_date = datetime.strptime(end_date, '%Y/%m')
# search_time = f"{end_date.strftime('%Y/%m')}/01"
# last_day = end_date.replace(day=1) + relativedelta(day=31)
# last_day = f"{last_day.strftime('%Y/%m/%d')}"
# element.send_keys(search_time)


# element.send_keys("8-Dec-2014")
# element.send_keys('2021/08' +' - '+ '2021/08')
# print("Then send key:"+b)

# element.send_keys(search_time+'-'+search_time)
# driver.find_element_by_xpath('/html/body/div[3]/div[4]/button[2]').click()
