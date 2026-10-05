import os
import subprocess
import webbrowser
import platform
import ipaddress
from dotenv import load_dotenv

load_dotenv()


def oupree():
    user_input = input(
        "\nEnter 1 for Israel boxes"
        "\n2 for US boxes"
        "\n3 for SA boxes"
        "\n4 for Russian boxes"
        "\n5 for Euro channels"
        "\nSelection: "
    ).strip()

    if user_input == "1":
        url = os.getenv("ISRAEL_OUPREE")
        print(url)
        webbrowser.open("https://" + url)

    elif user_input == "2":
        url = os.getenv("US_OUPREE")
        print(url)
        webbrowser.open("https://" + url)

    elif user_input == "3":
        url = os.getenv("SOUTHAFRICA_OUPREE")
        print(url)
        webbrowser.open("https://" + url)

    elif user_input == "4":
        russian_box = os.getenv("RUSSIAN_OUPREE")
        print(russian_box)

        if platform.system() == "Windows":
            subprocess.Popen(["mstsc", f"/v:{russian_box}"])

        else:
            print("Russian remote desktop is configured for Windows.")
            print("You are currently running this application on macOS.")

    elif user_input == "5":
        url = os.getenv("EURO_OUPREE")
        print(url)
        webbrowser.open("https://" + url)

    else:
        print("Invalid selection.")
