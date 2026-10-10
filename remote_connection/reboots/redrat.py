import os
import subprocess
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from remote_connection.config import REMOTE_LOCATIONS

load_dotenv()


REMOTE_IP = os.getenv("SAINFILED_DESKTOP")
USERNAME = os.getenv("SAINFILED_USERNAME")
PASSWORD = os.getenv("SAINFILED_PASSWORD")


def launch_remote_desktop():
    print("Web operation successful! Starting Remote Desktop...")
    try:
        cmdkey_add = (
            f"cmdkey /generic:TERMSRV/{REMOTE_IP} /user:{USERNAME} /pass:{PASSWORD}"
        )
        subprocess.run(cmdkey_add, shell=True, check=True)

        subprocess.Popen(f"mstsc.exe /v:{REMOTE_IP}", shell=True)

        time.sleep(3)
        subprocess.run(f"cmdkey /delete:TERMSRV/{REMOTE_IP}", shell=True, check=True)

    except Exception as e:
        print(f"Failed to launch RDP: {e}")


def run_web_operation(TARGET_URL):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(TARGET_URL)

        print("Waiting for web operation to finish...")

        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, "success-message"))
        )

        launch_remote_desktop()

    except Exception as e:
        print(f"Web operation failed or timed out: {e}")

    finally:
        driver.quit()


def redrat():
    while True:
        user_input = input(
            f"\nEnter 1 for {REMOTE_LOCATIONS['1']} boxes"
            f"\n2 for {REMOTE_LOCATIONS['2']} boxes"
            f"\n3 for {REMOTE_LOCATIONS['3']} boxes"
            f"\n4 for {REMOTE_LOCATIONS['4']} boxes"
            f"\n5 for {REMOTE_LOCATIONS['5']} boxes"
            f"\n6 for {REMOTE_LOCATIONS['6']} boxes"
            "\nSelection: "
        ).strip()

        print(
            f"Connecting to {REMOTE_LOCATIONS.get(user_input, 'Invalid selection.')} box"
        )
        base_ip = os.getenv(f"{REMOTE_LOCATIONS.get(user_input)}_REDRAT")
        TARGET_URL = f"https://{base_ip}"
        print(f"Target URL: {TARGET_URL}")
        run_web_operation(TARGET_URL)


def launch_remote_desktop():
    print("Web process restarted! Opening Remote Desktop...")
    try:
        # Inject credentials into Windows Credential Manager
        subprocess.run(
            f"cmdkey /generic:TERMSRV/{REMOTE_IP} /user:{USERNAME} /pass:{PASSWORD}",
            shell=True,
            check=True,
        )
        # Launch Windows RDP Client
        subprocess.Popen(f"mstsc.exe /v:{REMOTE_IP}", shell=True)
        time.sleep(3)
        # Clean up credentials
        subprocess.run(f"cmdkey /delete:TERMSRV/{REMOTE_IP}", shell=True, check=True)
    except Exception as e:
        print(f"Failed to launch RDP: {e}")


# --- WEB AUTOMATION ---
def restart_and_connect():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 30)  # Max wait time of 30 seconds per button

    try:
        driver.get(TARGET_URL)

        # 1. Click the first button (e.g., "Manage Process" or "Stop")
        # Change By.ID to By.XPATH or By.CSS_SELECTOR depending on your website
        first_button = wait.until(
            EC.element_to_be_clickable((By.ID, "first-button-id"))
        )
        first_button.click()
        print("Clicked first button.")

        # 2. Click the second button (e.g., "Confirm Restart" or "Start")
        second_button = wait.until(
            EC.element_to_be_clickable((By.ID, "second-button-id"))
        )
        second_button.click()
        print("Clicked second button.")

        # 3. Launch RDP immediately after the second click
        launch_remote_desktop()

    except Exception as e:
        print(f"Automation failed: {e}")
    finally:
        driver.quit()
