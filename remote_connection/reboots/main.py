from remote_connection.reboots.redrat import redrat
from remote_connection.reboots.oupree import oupree2


def main():
    user_input = input("\nType 1 for redrat\nType2 for oupree:  ")
    redrat() if user_input == "1" else oupree2()


if __name__ == "__main__":
    main()
