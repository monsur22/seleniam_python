import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
import os
from os import name
from selenium.webdriver.chrome.options import Options

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

# driver.find_element_by_class_name("btn-reset").click()

# driver.get("https://ad.rms.rakuten.co.jp/cpnadv/download_history")

driver.find_element_by_class_name("btn-reset").click()
driver.get("https://ad.rms.rakuten.co.jp/rpp/reports")

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[1]/div/div[1]/table/tbody/tr[1]/td/div/label[1]/input[@type='radio'][@value='1']"))).click()
time.sleep(5)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='prmm-rpp-report-table']/tbody/tr[2]/td/div[1]/label[1]/input[@type='radio'][@value='1']"))).click()
time.sleep(5)

start = driver.find_element_by_class_name("datepicker")
start.clear()
start.send_keys("2021-09")


time.sleep(3)
end = driver.find_element_by_id("prmm-rpp-report-datepicker-end")
end.clear()
end.send_keys("2021-11")


WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='prmm-rpp-search-criteria-div']/div[11]/button[2]"))).click() #click on search button

# driver.find_element_by_css_selector("span[class='ng-scope']").click()
time.sleep(10)

# Obtain button by link text and click.
button = driver.find_element_by_link_text("ダウンロード")
button.click()
