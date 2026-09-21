import subprocess
import os
from dotenv import load_dotenv

load_dotenv()
st = os.getenv("STAT")
dl = os.getenv("DSC")
isr = os.getenv("ISRAEL")
links = [dl, st, isr]
strlink = ["dl", "st", "isr"]


def playback():
<<<<<<< HEAD

    source = input("type input source (dl / st/ isr): ").lower()
    channel_no = input("type channel number ")

    if source in strlink:
        index = strlink.index(source)
        lnk = links[index]
        lnk += channel_no
        print(lnk)
        command = ["ffplay", "-autoexit", "-loglevel", "debug", lnk]
        subprocess.run(command, check=True)
=======
    source = input("type input source (dl / st/ isr): ").lower()
    channel_no = input("type channel number:  ")
    while True:
        if source in strlink and channel_no != "exit":
            index = strlink.index(source)
            lnk = links[index]
            lnk += channel_no
            print(lnk)
            command = ["ffplay", "-autoexit", "-loglevel", "debug", lnk]
            subprocess.run(command, check=True)

        else:
            print("Invalid source. Please enter 'dl', 'st', or 'isr'.")

        channel_no = input("enter another channel number  or q to quit: ")
        if channel_no.lower() == "q":
            print("Exiting the program.")
            break
>>>>>>> feature


playback()
