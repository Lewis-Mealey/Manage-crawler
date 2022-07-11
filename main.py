import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

Path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(Path)

Path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(Path)

driver.get("https://chrome.google.com/webstore/detail/windows-accounts/ppnbnpeolgkicgegkbkbjmhlideopiji")

try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "g-c-Hf"))
    )
finally:
    search = driver.find_element(By.CLASS_NAME, "g-c-Hf")
    search.click()

time.sleep(5)

driver.get("https://manage.nitec.com")

# try:
#     element = WebDriverWait(driver, 1000).until(
#         EC.presence_of_element_located((By.ID, "Company_Name-input"))
#     )
# finally:
#     search = driver.find_element(By.ID, "Company_Name-input")
#     search.send_keys(Keys.RETURN)
#
# try:
#     element = WebDriverWait(driver, 1000).until(
#         EC.presence_of_element_located(("id", "Company_Type_RecID"))
#     )
# finally:
#     search = Select(driver.find_element("id", 'Company_Type_RecID'))
#     search.select_by_visible_text('Customer')

time.sleep(1000)