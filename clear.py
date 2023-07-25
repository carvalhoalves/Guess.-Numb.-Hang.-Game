from os import name, system
from time import sleep


def clear_screen():
    sleep(.25)

    if name == 'nt':
        _ = system('cls')
        #
        # Windows
    else:
        _ = system('clear')
        #
        # Linux, MacOS
