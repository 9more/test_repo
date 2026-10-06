from dotenv import load_dotenv
import webbrowser
import os
import subprocess
import ipaddress

from h11 import CLIENT
from virtuals.config import CLIENT_CATEGORIES, CLIENTS, SOURCE

load_dotenv()


def online():
    while True:

        source = input(
            "\nType 1 for BETFRED"
            "\nType 2 for CORAL"
            "\nType 3 for LADBROKES"
            "\nType 4 for HIGHLIGHT GAMES"
            "\nType 5 for KIRON  "
        ).strip()

        if source == "1":
            print("\nBETFRED VIRTUAL CATEGORIES:")
            for key, value in CLIENT_CATEGORIES["BETFRED"].items():
                print(f"Type {key} for {value}")
            vgen = int(input("\nEnter a VGEN to remote into: "))

            while True:
                while vgen not in CLIENT_CATEGORIES["BETFRED"]:
                    print("Invalid VGEN selection.")
                    vgen = int(input("\nEnter a valid VGEN to remote into: "))
                print(
                    f"Name of selected Virtual Sport: VGEN{str(vgen)}-- {CLIENT_CATEGORIES['BETFRED'][vgen]}"
                )
                base_ip = os.getenv("BETFRED_INSPIRED_ONLINE")

                if not base_ip:
                    print("BETFRED_INSPIRED_ONLINE is not configured.")

                try:
                    ip = ipaddress.ip_address(base_ip)
                    target_ip = ip + vgen

                    print(f"Remote IP: {target_ip}")

                except ValueError:
                    print(f"Invalid IP address: {base_ip}")

                question = input(
                    "\nWould you like to check another Betrfred Controller? y=YES, n=NO  "
                ).lower()
                if question == "n":
                    break
                else:
                    vgen = int(input("\nEnter another VGEN to remote into: "))

        elif source == "2":
            print("\nCORAL VIRTUAL CATEGORIES:")
            for key, value in CLIENT_CATEGORIES["CORAL"].items():
                print(f"Type {key} for {value}")
            cvgen = int(input("\nEnter a CVGEN to remote into: "))

            while True:
                if cvgen not in CLIENT_CATEGORIES["CORAL"]:
                    print("Invalid CVGEN selection.")
                    cvgen = int(input("\nEnter a valid CVGEN to remote into: "))
                print(
                    f"Name of selected Virtual Sport: CVGEN{str(cvgen)}-- {CLIENT_CATEGORIES['CORAL'][cvgen]}"
                )
                base_ip = os.getenv("CORAL_INSPIRED_ONLINE")
                if not base_ip:
                    print("CORAL_INSPIRED_ONLINE is not configured.")

                try:
                    ip = ipaddress.ip_address(base_ip)
                    target_ip = ip + cvgen

                    print(f"Remote IP: {target_ip}")

                except ValueError:
                    print(f"Invalid IP address: {base_ip}")
                question = input(
                    "\nWould you like to check another Coral Controller? y=YES, n=NO  "
                ).lower()
                if question == "n":
                    break
                else:
                    cvgen = int(input("\nEnter another CVGEN to remote into: "))

        elif source == "3":
            print("\nLADBROKES VIRTUAL CATEGORIES:")
            for key, value in CLIENT_CATEGORIES["LADBROKES"].items():
                print(f"Type {key} for {value}")
            lvgen = int(input("\nEnter a LVGEN to remote into: "))

            while True:
                if lvgen not in CLIENT_CATEGORIES["LADBROKES"]:
                    print("Invalid LVGEN selection.")
                    lvgen = int(input("\nEnter a valid LVGEN to remote into: "))
                print(
                    f"Name of selected Virtual Sport: LVGEN{str(lvgen)}-- {CLIENT_CATEGORIES['LADBROKES'][lvgen]}"
                )
                print()
                base_ip = os.getenv("LADBROKES_INSPIRED_ONLINE")
                if not base_ip:
                    print("LADBROKES_INSPIRED_ONLINE is not configured.")

                try:
                    ip = ipaddress.ip_address(base_ip)
                    target_ip = ip + lvgen

                    print(f"Remote IP: {target_ip}")

                except ValueError:
                    print(f"Invalid IP address: {base_ip}")

                question = input(
                    "\nWould you like to check another Ladbrokes Controller? y=YES, n=NO "
                ).lower()
                if question == "n":
                    break
                else:
                    lvgen = int(input("\nEnter another LVGEN to remote into: "))
        elif source == "4":
            url = os.getenv("HIGHLIGHT_GAMES")
            print(url)
            webbrowser.open("https://" + url)
        elif source == "5":
            url = os.getenv("KIRON")
            print(url)
            webbrowser.open("https://" + url)

        check_another_source = input("\nEnter q to quit or c to continue..  ").lower()
        if check_another_source == "q":
            break


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
                print(f"\n{CLIENTS[client]} {CLIENTS['1']} VIRTUAL CATEGORIES:")
                for key, value in CLIENT_CATEGORIES[CLIENTS[client]].items():
                    print(f"Type {key} for {value}")
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

                    except ValueError:
                        print(f"Invalid IP address: {base_ip}")

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


online2()
