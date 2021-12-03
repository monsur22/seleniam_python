import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from datetime import datetime
from dateutil.relativedelta import relativedelta, MO

driver = webdriver.Chrome(
    'C:/webdriver/chromedriver.exe')
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

driver.find_element_by_class_name("btn-reset").click()
driver.get("https://ad.rms.rakuten.co.jp/cpnadv/performance_reports")



# driver.find_element_by_xpath("//*[@id='prmm-cpnadv-performance-report-table']/div[1]/table/tbody/tr[1]/td/table/tbody/tr/td[2]/label/input").click()
# print('click first button')
driver.find_element_by_xpath("//*[@id='prmm-cpnadv-performance-report-table']/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/label/input").click()
print('click secont  button')


# end_date = driver.find_element_by_id("prmm-cpnadv-report-start-date").send_keys("2021-01")
# print(end_date)

# end_date = '2021-01'
# print(end_date)

# end_date = driver.data['end_date']
# end_date = end_date[0:7]
# end_date = datetime.strptime(end_date, '%Y-%m')
# end_time = f"{end_date.strftime('%Y-%m')}"
# start_time = end_date - relativedelta(months=2)
# start_time = f"{start_time .strftime('%Y-%m')}"

# driver.find_element_by_id("prmm-cpnadv-report-start-date").send_keys(end_time)

# print("printing end date")
# print(start_time)
# print(end_time)



# driver.get("https://ad.rms.rakuten.co.jp/cpnadv/download_history")

# time.sleep(10)

# # Obtain button by link text and click.
# button = driver.find_element_by_link_text("ダウンロード")
# button.click()
