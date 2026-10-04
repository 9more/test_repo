from redrat import redrat
from oupree import oupree


def main():
    user_imput = input("enter  1 for redrat\n2 for oupree:  ")
    redrat() if user_imput == "1" else oupree()


if __name__ == "__main__":
    main()
