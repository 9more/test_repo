import subprocess


def playback():
    stats = "srt://primary-spingest.igamemedia.com:190"
    dsc = "rtmp://10.10.71.1/contrib/INF_IGM_Ch "
    source = input("type input source  ").lower()

    if source == "downlink":
        channel_no = input("type channel number ")
        stats += str(channel_no)
        print(stats)

        command = ["ffplay", "-aotoexit", stats]
        subprocess.run(command, check=True)

    else:
        pass


playback()
