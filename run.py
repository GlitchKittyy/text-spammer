from colorama import Fore
from os import name, system
import sys
from time import sleep

def spammer():
    clear()
    printBanner()
    words = Fore.YELLOW + "[" + Fore.WHITE + "·" + Fore.YELLOW + "]" + Fore.BLUE + " Enter the word you want to use\n"
    for char in words:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()

    word = input(Fore.RED + "[" + Fore.WHITE + "+" + Fore.RED + "]" + Fore.WHITE + " ")
    wordList = list(word)

    repetition_dict = {}

    for i, char in enumerate(wordList):
        times = int(input(Fore.GREEN + "[" + Fore.WHITE + "?" + Fore.GREEN + "]" + Fore.WHITE + f" How many times do you want '{char}' at position {i+1} | "))
        repetition_dict[char + str(i+1)] = times
    
    result_segments = []
    for i, char in enumerate(wordList):
        count = repetition_dict.get(char + str(i+1), 1)
        result_segments.append(char * count)
    
    result_word = ''.join(result_segments)
    sleep(1)
    clear()
    printBanner()
    print(Fore.RED+"\n\nResult:\n"+Fore.WHITE)
    sleep(1)
    print(result_word)
    sleep(1)
    words = Fore.YELLOW + "\n[" + Fore.WHITE + "·" + Fore.YELLOW + "]" + Fore.BLUE + " Thanks for using my program!\n\n"
    for char in words:
        sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()
    sleep(2)
    exit()

def clear():
   if name == 'nt':
        _ = system('cls') 
   else:
        _ = system('clear')

def printBanner():
    banner = """
   ▄▄▄▄▄   █ ▄▄  ██   █▀▄▀█ █▀▄▀█ ▄███▄   █▄▄▄▄
  █     ▀▄ █   █ █ █  █ █ █ █ █ █ █▀   ▀  █  ▄▀
▄  ▀▀▀▀▄   █▀▀▀  █▄▄█ █ ▄ █ █ ▄ █ ██▄▄    █▀▀▌ 
 ▀▄▄▄▄▀    █     █  █ █   █ █   █ █▄   ▄▀ █  █ 
            █       █    █     █  ▀███▀     █  
             ▀     █    ▀     ▀            ▀   
                  ▀                               
 By GlitchKittyy                                   
"""
    gradient_colors = [Fore.RED, Fore.LIGHTRED_EX]
    for i, line in enumerate(banner.split('\n')):
        print(gradient_colors[i % len(gradient_colors)], line)

def menu():
    clear()
    printBanner()
    print(f"\n\n\n1. Text Spammer\n2. How to use\n3. About\n4. Exit\n\n")
    choice = int(input("Enter Choice: "))
    while choice > 4:
        clear()
        printBanner()
        print(f"\n\n\n1. Text Spammer\n2. How to use\n3. About\n4. Exit\n\n")
        choice = int(input("Enter Choice: "))
    if choice == 1:
        spammer()


menu()
