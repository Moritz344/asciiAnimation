import os
import random
import time
from termcolor import colored,cprint

def clearScreen():
    os.system("clear")

def hideCursor():
    print("\033[?25l", end="", flush=True)
def showCursor():
    print("\033[?25h", end="", flush=True)

def main():
    clearScreen()
    hideCursor()
    
    cprint("Select from 1-3","yellow")
    speedInput = input("Speed: ")
    speedInput = int(speedInput)

    width = 150 
    height = 30

    chars = ["*","+"]
    #chars = [colored("*","white"),colored("+","white")]

    # Wir Erstellen eine Spalte mit Höhe 1-30 und der Breite 150
    columns = [random.randint(1,height) for _ in range(width)]
    try:
        while True:
            for x in range(width):
                print(f"\033[{columns[x]};{x}H{random.choice(chars)}",flush=True)

                columns[x] += speedInput

                if columns[x] > height:
                    columns[x] = 1

            time.sleep(0.1)
            clearScreen()

    except KeyboardInterrupt:
        clearScreen()

        

main()



