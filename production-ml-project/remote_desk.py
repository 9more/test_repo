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

go_to = ["oupree", "redrat"]
regions = ["isrea", "russia", "australia"]

destin = input("what destinationation would you want to restart? oupree or redrat")
dest_confirm = input("type the destination again to comfirm...")
if destin != dest_confirm:
    print(
        "This program has been terminated because the destination cannot be confrim, please try again"
    )
    sys.exit(1)
remote_site = input("type the destination again to comfirm...")
remote_site_confirm = input("type the remote site confirmation again to comfirm...")
if remote_site != remote_site_confirm:
    print(
        "This program has been terminated because the destination cannot be confrim, please try again"
    )
    sys.exit(1)

device = input("type stb no")
device_confirm=input("onfirmation stb...")
username = os.getenv((remote_site + "_username").upper())
password = os.getenv((remote_site + "_password").upper())
ip = os.getenv((remote_site + "_ip_address").upper())
if destin == "oupree":
    if remote_site in regions:
        pass


elif destin == "redrat":
    pass
