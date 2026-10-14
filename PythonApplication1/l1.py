import os
import time
import math

red = "\033[41m  \033[0m"
white = "\033[47m  \033[0m"
print(red * 5)
print(red * 2 + white + red * 2)
print(red + white * 3 + red)
print(red * 2 + white + red * 2)
print(red * 5)

pattern = "\033[47m" + "\033[30mOO\033[0m"
print(pattern * 5)

def animate():
    frames = [
        "  o  \n /|\\ \n / \\ ",
        "  o  \n /|\\ \n  |  ",
        "  o  \n /|\\ \n / \\ ",
        "  o/ \n  |  \n / \\ "
    ]
    
    try:
        for frame in frames:
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
            
            print("anim")
            print(frame)
            time.sleep(0.8)
    except KeyboardInterrupt:
        print("\na")