import webbrowser
import os
import time
from dotenv import load_dotenv
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()
username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")

options = uc.ChromeOptions()
driver = uc.Chrome(options=options)

driver.get("https://engage.aminoengage.com/engage/#device/listEngage")

wait = WebDriverWait(driver, 1500)
username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
password_field = driver.find_element(By.NAME, "password")

username_field.send_keys(username)
password_field.send_keys(password)
password_field.send_keys(Keys.ENTER)

print("Logged in successfully!")
print(
    "The script has finished executing, but the browser window will stay open forever!"
)
# Keep this at the absolute bottom of your script
input("Press Enter to close the browser...")
