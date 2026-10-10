from dotenv import load_dotenv
import webbrowser
import os
import subprocess
import ipaddress
from remote_connection.config import CLIENT_CATEGORIES, CLIENTS, SOURCE

load_dotenv()


def online2():
    while True:
        source = input(
            f"\nType 1 for {SOURCE['1']}"
            f"\nType 2 for {SOURCE['2']}"
            f"\nType 3 for {SOURCE['3']}\n"
        ).strip()
        if source == "1":
            while True:
                client = input(
                    f"\nType 1 for {CLIENTS['1']}"
                    f"\nType 2 for {CLIENTS['2']}"
                    f"\nType 3 for {CLIENTS['3']}\n"
                ).strip()
                if client in CLIENTS:
                    print(f"\nYou selected {CLIENTS[client]}")
                else:
                    print("Invalid selection. Please choose a valid client.")
                    continue
                print(f"\n{CLIENTS[client]} {SOURCE['1']} VIRTUAL CATEGORIES:")
                for key, value in CLIENT_CATEGORIES[CLIENTS[client]].items():
                    print(
                        f"Type {key} for VGEN{key}-- {value}"
                        if client == "1"
                        else f"Type {key} for {CLIENTS[client][0]}VGEN{key}-- {value}"
                    )
                vgen = int(input("\nEnter a VGEN to remote into: "))

                while True:
                    if vgen not in CLIENT_CATEGORIES[CLIENTS[client]]:
                        print("Invalid VGEN selection.")
                        vgen = int(input("\nEnter a valid VGEN to remote into: "))
                    print(
                        f"Name of selected Virtual Sport: VGEN{str(vgen)}-- {CLIENT_CATEGORIES[CLIENTS[client]][vgen]}"
                    )
                    base_ip = os.getenv(str(CLIENTS[client]) + "_INSPIRED_ONLINE")

                    if not base_ip:
                        print(f"{CLIENTS[client]}_INSPIRED_ONLINE is not configured.")

                    try:
                        ip = ipaddress.ip_address(base_ip)
                        target_ip = ip + vgen

                        print(f"Remote IP: {target_ip}")
                        # Default installation path for TightVNC on Windows (adjust path/version if needed)
                        tightvnc_path = r"C:\Program Files\TightVNC\tvncviewer.exe"

                        # Optional: target host and port (e.g., 192.168.1.50:5901)
                        # Open TightVNC Viewer as a separate process
                        subprocess.Popen([tightvnc_path, str(target_ip)])

                    except ValueError:
                        print(f"Invalid IP address: {base_ip}")
                        print("TightVNC Viewer started successfully.")
                        print(
                            f"Error: TightVNC executable not found at '{tightvnc_path}'. Please check"
                            " your installation path."
                        )

                    question = input(
                        f"\nWould you like to check another {CLIENTS[client]} Controller? y=YES, n=NO  "
                    ).lower()
                    if question == "n":
                        break
                    else:
                        vgen = int(input("\nEnter another VGEN to remote into: "))
                questiom = input(
                    "\nWould you like to check another Inspire Client? y=YES, n=NO "
                ).lower()
                if questiom == "n":
                    break

        elif source == "2":
            url = os.getenv("KIRON")
            print(url)
            webbrowser.open("https://" + url)

        elif source == "3":
            url = os.getenv("HIGHLIGHT_GAMES")
            print(url)
            webbrowser.open("https://" + url)

        questiom = input(
            "\nWould you like to check another source? y=YES, n=NO  "
        ).lower()
        if questiom == "n":
            break
