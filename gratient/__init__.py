# Module made by @venaxyt on Github
from os import system

def purple(text):
    system(""); faded = ""
    for line in text.splitlines():
        red = 35
        for character in line:
            red += 3
            if red > 255:
                red = 255
            faded += (f"\033[38;2;{red};0;220m{character}\033[0m")
        faded += "\n"
    return faded
