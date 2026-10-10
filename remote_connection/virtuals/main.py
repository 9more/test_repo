from remote_connection.virtuals.online_virtuals import online2
from remote_connection.virtuals.retail_virtual import retail


def main():

    user = input("\n1 for ONLINE" "\n2 for RETAIL\n").strip()
    online2() if user == "1" else retail()


if __name__ == "__main__":
    main()
