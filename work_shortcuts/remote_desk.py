import webbrowser
import os
import time
import sys
from dotenv import load_dotenv
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

regions = ["isreal", "russia", "australia"]

destin = input("what destinationation would you want to restart?\n oupree or redrat...")
dest_confirmation = input("type the destination again to comfirm...")
if destin != dest_confirmation:
    print(
        "This program has been terminated because the destination cannot be confrim, please try again"
    )
    sys.exit(1)
remote_site = input("region :isrea, russia, or australia ?...")
remote_confirmation = input("type the region again to comfirm...")
if destin != dest_confirmation:
    print(
        "This program has been terminated because the remote site cannot be confrim, please try again"
    )
    sys.exit(1)


device = input(r"type stb no...\n")

username = os.getenv((remote_site + "_username").upper())
print(username)
password = os.getenv((remote_site + "_password").upper())
ip = os.getenv((remote_site + "_ip_address").upper())
if destin == "oupree":
    if remote_site in regions:
        pass


elif destin == "redrat":
    pass
