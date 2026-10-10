from remote_connection.reboots.main import main
from remote_connection.virtuals.main import main as virtuals_main

if __name__ == "__main__":
    user_input = input(
        "\nType 1 for STB REBOOTS\nType 2 for VIRTUALS\nSelection: "
    ).strip()
    main() if user_input == "1" else virtuals_main()
