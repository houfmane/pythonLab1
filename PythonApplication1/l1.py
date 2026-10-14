import os
import time
import math

red = "\033[41m"
green = "\033[42m"
yellow = "\033[43m"
reset =  "\033[0m"

erase = "\x1B[2K"
begin = "\x1B[1G"

def flag():
    pixel = "  "
    whitePixel = "\033[47m  \033[0m"
    print((red + pixel) * 5 + reset)
    print((red + pixel) * 2 + whitePixel + (red + pixel) * 2 + reset)
    print((red + pixel) + whitePixel * 3 + (red + pixel) + reset)
    print((red + pixel) * 2 + whitePixel + (red + pixel) * 2 + reset)
    print((red + pixel) * 5 + reset)

def pattern():
    pat = "\033[47m" + "\033[30mOO\033[0m"
    print(pat * 5)

def loading():
    for i in range(100):
        print("\u001b[20Dloading..." + str(i + 1), end='', flush=True)
        time.sleep(0.1)
    print("done")

def progressbar(tasks = 3):
    bar_lenth = 25
    for task in range(1, tasks + 1):
        for p in range(1, bar_lenth + 1):
            colour = green
            if p / bar_lenth < 0.3:
                colour = red
            elif p / bar_lenth != 1:
                colour = yellow

            bar = colour + "#" * p + reset + "_" * (bar_lenth - p)
            print(f'{begin}{erase}Task {task}/{tasks} [{bar}] {p * 4}%', end='', flush=True)
            time.sleep(0.04)
        print(f'{begin}{erase}Task {task}/{tasks} [{bar}] {p * 4}%')
    print("done")

def sequence():
    file = open('sequence.txt', 'r')
    l1 = []
    l2 = []

    for line in file:
        if abs(float(line)) <= 3:
            l1.append(float(line))
        else:
            l2.append(float(line))

    print(f'{red}{" " * int(len(l1) / 5)}{reset} {len(l1) / (len(l1) + len(l2)) * 100}%') 
    print(f'{green}{" " * int(len(l2) / 5)}{reset} {len(l2) / (len(l1) + len(l2)) * 100}%')

    file.close()

flag()
pattern()
progressbar()
sequence()
