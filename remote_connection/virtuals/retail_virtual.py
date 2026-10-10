import os
import subprocess
import webbrowser
import ipaddress
from dotenv import load_dotenv
from remote_connection.config import CLIENTS, RETAIL_CATEGORIES, SOURCE

load_dotenv()


def retail():
    source = input(
        f"\nType 1 for {SOURCE['1']}_RETAIL"
        f"\nType 2 for {SOURCE['3']}_RETAIL\nSelection: "
    ).strip()
    if source == "1":
        for key, value in RETAIL_CATEGORIES[SOURCE["1"]].items():
            print(f"Type {key} for {value}")
        controller = input(f"\nEnter a controller to remote into: \n").strip()
        base_ip = os.getenv(f"{SOURCE[source]}_RETAIL")
        vnc_password = os.getenv("CONTROLLER_PASSPORD")
        new_ip_address = ipaddress.ip_address(base_ip) + int(controller)
        print(
            f"Connecting to {RETAIL_CATEGORIES[SOURCE['1']][controller]} at IP address {new_ip_address}"
        )

        tightvnc_path = r"C:\Program Files\TightVNC\tvncviewer.exe"
        try:
            subprocess.Popen(
                [tightvnc_path, str(new_ip_address), "-password", str(vnc_password)]
            )
            print("TightVNC Viewer started and password passed.")
        except NotADirectoryError:
            print(
                "Error: TightVNC executable not found. Verify your installation path."
            )

    else:
        for key, value in RETAIL_CATEGORIES[SOURCE["3"]].items():
            print(f"Type {key} for {value}")
        controller = input(f"\nEnter a controller to remote into: \n").strip()
        base_url = os.getenv(f"{SOURCE['3']}_RETAIL")
        new_ip_address = base_url + controller
        print(
            f"Connecting to {RETAIL_CATEGORIES[SOURCE['3']][controller]} at IP address {new_ip_address}"
        )
        subprocess.Popen(
            ["ffplay", "-i", new_ip_address],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            stdin=subprocess.DEVNULL,
            close_fds=True,
        )
