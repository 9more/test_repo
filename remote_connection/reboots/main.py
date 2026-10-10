from remote_connection.reboots.redrat import redrat
from remote_connection.reboots.oupree import oupree2


def main():
    user_input = input("\nType 1 for REDRAT\nType 2 for OUPREE\nSelection: ").strip()
    redrat() if user_input == "1" else oupree2()


if __name__ == "__main__":
    main()
