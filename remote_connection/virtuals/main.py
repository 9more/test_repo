from online_virtuals import online
from retail_virtual import retail


def main():

    user = input("\n1 for ONLINE" "\n2 for RETAIL: ")
    online() if user == "1" else retail()


if __name__ == "__main__":
    main()
