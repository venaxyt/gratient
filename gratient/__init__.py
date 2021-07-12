# Module made by @venaxyt on Github
from os import system


def black(text):
    system(""); faded = ""
    for line in text.splitlines():
        red = 0; green = 0; blue = 0
        for character in line:
            red += 3; green += 3; blue += 3
            if red > 255 and green > 255 and blue > 255:
                red = 255; green = 255; blue = 255
            faded += (f"\033[38;2;{red};{green};{blue}m{character}\033[0m")
        faded += "\n"
    return faded

def green(text):
    system(""); faded = ""
    for line in text.splitlines():
        blue = 100
        for character in line:
            blue += 2
            if blue > 255:
                blue = 255
            faded += (f"\033[38;2;0;255;{blue}m{character}\033[0m")
        faded += "\n"
    return faded

def blue(text):
    system(""); faded = ""
    for line in text.splitlines():
        green = 0
        for character in line:
            green += 3
            if green > 255:
                green = 255
            faded += (f"\033[38;2;0;{green};255m{character}\033[0m")
        faded += "\n"
    return faded

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

def yellow(text):
    system(""); faded = ""
    for line in text.splitlines():
        red = 0
        for character in line:
            if not red > 200:
                red += 3
            faded += (f"\033[38;2;{red};255;0m{character}\033[0m")
        faded += "\n"
    return faded

def red(text):
    system(""); faded = ""
    for line in text.splitlines():
        green = 250
        for character in line:
            green -= 5
            if green < 0:
                green = 0
            faded += (f"\033[38;2;255;{green};0m{character}\033[0m")
        faded += "\n"
    return faded
