#!/usr/bin/env python3
from colorama import init, Fore

def display(message, is_warning=False):
    if is_warning:
        print(Fore.RED + message)
    else:
        print(Fore.BLUE + message)
        