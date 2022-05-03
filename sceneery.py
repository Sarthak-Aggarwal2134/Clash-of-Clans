from colorama import Fore, Back, Style
from glo_var import *
import time
HEALTH_KING=100
class scene():
    def __init__(self):
        self._lives=1
        self._score=0
        self._level=1
        self._start=int(time.time())


    def print_grid(x,townhall,walls,cannons,huts,king,wizards,avatar):
        for row in range(rows):
            for col in range(cols):
                if colr[row][col]=="BLUE":
                    print(Back.BLUE,end="")
                if ar[row][col] == 'T':
                    if townhall.health>250:
                        print(Fore.GREEN + ar[row][col] + Style.RESET_ALL, end="")
                    elif townhall.health>100:
                        print(Fore.YELLOW + ar[row][col] + Style.RESET_ALL, end="")
                    else:
                        print(Fore.RED + ar[row][col] + Style.RESET_ALL, end="")
                elif ar[row][col] == 'C':
                    ind = int(arr2[row][col][6])-1
                    if cannons[ind].active == True:
                        print(Back.LIGHTWHITE_EX, end="")
                    if cannons[ind].health>=15:
                        print(Fore.GREEN + ar[row][col] + Style.RESET_ALL, end="")
                    elif cannons[ind].health>=10:
                        print(Fore.YELLOW + ar[row][col] + Style.RESET_ALL, end="")
                    else:
                        print(Fore.RED + ar[row][col] + Style.RESET_ALL, end="")
                    print(Back.RESET, end="")
                elif ar[row][col]=='H':
                    ind = int(arr2[row][col][3])-1
                    if huts[ind].health>=30:
                        print(Fore.GREEN + ar[row][col] + Style.RESET_ALL, end="")
                    elif huts[ind].health>=20:
                        print(Fore.YELLOW + ar[row][col] + Style.RESET_ALL, end="")
                    else:
                        print(Fore.RED + ar[row][col] + Style.RESET_ALL, end="")
                elif ar[row][col]=='X':
                    ind = int(arr2[row][col][6])-1
                    if wizards[ind].active == True:
                        print(Back.LIGHTWHITE_EX, end="")
                    if wizards[ind].health>=15:
                        print(Fore.GREEN + ar[row][col] + Style.RESET_ALL, end="")
                    elif wizards[ind].health>=10:
                        print(Fore.YELLOW + ar[row][col] + Style.RESET_ALL, end="")
                    else:
                        print(Fore.RED + ar[row][col] + Style.RESET_ALL, end="")
                    print(Back.RESET, end="")
                else:
                    if(ar[row][col]=='K' and avatar=='q'):
                        print('Q',end="")
                    else:
                        print(ar[row][col], end="")
                
                if colr[row][col]=="BLUE":
                    colr[row][col]=" "
                    print(Back.RESET,end="")
            print()
        healthDisplay = ' ' * int(king.king_health*10/HEALTH_KING)  
        remainingDisplay = ' ' * (10 - int(king.king_health*10/HEALTH_KING))
        print("King's Health : |" + Back.GREEN + healthDisplay + Back.RED + remainingDisplay + Back.RESET + "|" )
    