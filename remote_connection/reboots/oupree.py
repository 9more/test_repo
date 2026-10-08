import os
import subprocess
import webbrowser
import platform
import ipaddress
from dotenv import load_dotenv
from remote_connection.virtuals.config import REMOTE_LOCATIONS

load_dotenv()


def oupree2():
    while True:
        user_input = input(
            f"\nEnter 1 for {REMOTE_LOCATIONS['1']} boxes"
            f"\n2 for {REMOTE_LOCATIONS['2']} boxes"
            f"\n3 for {REMOTE_LOCATIONS['3']} boxes"
            f"\n4 for {REMOTE_LOCATIONS['4']} boxes"
            f"\n5 for {REMOTE_LOCATIONS['5']} channels"
            f"\n6 for {REMOTE_LOCATIONS['6']} channels"
            "\nSelection: "
        ).strip()

        while True:

            if user_input not in REMOTE_LOCATIONS:
                print("Invalid selection.")
                return

            if user_input == "4":
                russian_box = os.getenv(f"{REMOTE_LOCATIONS.get('4')}_OUPREE")
                print(russian_box)
                if platform.system() == "Windows":
                    subprocess.Popen(["mstsc", f"/v:{russian_box}"])

                else:
                    print("Russian remote desktop is configured for Windows.")
                    print("You are currently running this application on macOS.")
            else:
                box_number = input("Enter box number: ").strip()
                box = REMOTE_LOCATIONS.get(user_input, "Invalid selection.")
                if box == "Invalid selection.":
                    print("box not found")
                    continue
                base_ip = os.getenv(f"{box}_OUPREE")
                base_ip_address = ipaddress.ip_address(base_ip)
                new_ip_address = base_ip_address + int(box_number)
                print(
                    f"Connecting to {box} box number {box_number} at IP address: {new_ip_address}"
                )
                webbrowser.open(f"https://{new_ip_address}")
            question = (
                input("Do you want to connect to another box? (y/n): ").strip().lower()
            )
            if question != "y":
                print("Exiting the program.")
                break

        question = (
            input("Do you want to connect to another box? (y/n): ").strip().lower()
        )
        if question != "y":
            print("Exiting the program.")
            break
