from buildings import *
import os
from glo_var import *
from sceneery import *
from initial import *



class kings():
    def __init__(self,name,posx,posy):
        self.name=name
        self.king_x=posx
        self.king_y=posy
        self.king_lives=1
        self.king_score=0
        self.king_level=1
        self.king_health=100
        self.king_speed=1
        self.king_power=10

    def build(self):
        ar[self.king_x][self.king_y]='K'
        arr2[self.king_x][self.king_y]='K'

    def move(self,ch):
        for f in range(self.king_speed):
            ar[self.king_x][self.king_y]=' '
            arr2[self.king_x][self.king_y]=' '
            if ch=="a" and self.king_health>0:
                if arr2[self.king_x][self.king_y-1] == ' ':
                    self.king_y-=1
            elif ch=="d" and self.king_health>0:
                if arr2[self.king_x][self.king_y+1] == ' ':
                    self.king_y+=1
            elif ch=="w" and self.king_health>0:
                if arr2[self.king_x-1][self.king_y] == ' ':
                    self.king_x-=1
            elif ch=="s" and self.king_health>0:
                if arr2[self.king_x+1][self.king_y] == ' ':
                    self.king_x+=1
            ar[self.king_x][self.king_y]='K'
            arr2[self.king_x][self.king_y]='K'

    def attack(self,townhall,huts,cannons,walls,wizards,avatar,last_direction):
        if avatar=="k":
            if arr2[self.king_x][self.king_y+1] != ' ':
                if arr2[self.king_x][self.king_y+1][0] == 't':
                    townhall.health -= self.king_power
                    # os.system('aplay ./sound1.mp3&2>/dev/null')
                elif arr2[self.king_x][self.king_y+1][0] == 'w':
                    #print(arr[2])
                    # os.system('aplay ./sound1.mp3&2>/dev/null')
                    ind = 0
                    if len(arr2[self.king_x][self.king_y+1]) == 6:
                        ind = int(10*int(arr2[self.king_x][self.king_y+1][4]) + int(arr2[self.king_x][self.king_y+1][5])) - 1
                    else:
                        ind = int(arr2[self.king_x][self.king_y+1][4])-1
                    # print(ind)
                    walls[ind].health -= self.king_power
                elif arr2[self.king_x][self.king_y+1][0] == 'c':
                    ind = int(arr2[self.king_x][self.king_y+1][6])-1
                    cannons[ind].health -= self.king_power
                    # os.system('aplay ./sound1.mp3&2>/dev/null')
                elif arr2[self.king_x][self.king_y+1][0] == 'x':
                    ind = int(arr2[self.king_x][self.king_y+1][6])-1
                    wizards[ind].health -= self.king_power
                    # os.system('aplay ./sound1.mp3&2>/dev/null')
                elif arr2[self.king_x][self.king_y+1][0] == 'h':
                    ind = int(arr2[self.king_x][self.king_y+1][3])-1
                    huts[ind].health -= self.king_power
                    # os.system('aplay ./sound1.mp3&2>/dev/null')
            elif arr2[self.king_x][self.king_y-1] != ' ':
                if arr2[self.king_x][self.king_y-1][0] == 't':
                    townhall.health -= self.king_power
                    # os.system('aplay ./sound1.mp3&2>/dev/null')
                elif arr2[self.king_x][self.king_y-1][0] == 'w':
                    ind = 0
                    # os.system('aplay ./sound1.mp3&2>/dev/null')
                    if len(arr2[self.king_x][self.king_y-1]) == 6:
                        ind = int(10*int(arr2[self.king_x][self.king_y-1][4]) + int(arr2[self.king_x][self.king_y-1][5])) - 1
                    else:
                        ind = int(arr2[self.king_x][self.king_y-1][4])-1
                    # print(ind)
                    walls[ind].health -= self.king_power
                elif arr2[self.king_x][self.king_y-1][0] == 'c':
                    ind = int(arr2[self.king_x][self.king_y-1][6])-1
                    cannons[ind].health -= self.king_power
                    # os.system('aplay ./sound1.mp3&2>/dev/null')
                elif arr2[self.king_x][self.king_y-1][0] == 'x':
                    ind = int(arr2[self.king_x][self.king_y-1][6])-1
                    wizards[ind].health -= self.king_power
                    # os.system('aplay ./sound1.mp3&2>/dev/null')
                elif arr2[self.king_x][self.king_y-1][0] == 'h':
                    ind = int(arr2[self.king_x][self.king_y-1][3])-1
                    huts[ind].health -= self.king_power
                    # os.system('aplay ./sound1.mp3&2>/dev/null')
            elif arr2[self.king_x-1][self.king_y] != ' ':
                if arr2[self.king_x-1][self.king_y][0] == 't':
                    townhall.health -= self.king_power
                    # os.system('aplay ./sound1.mp3&2>/dev/null')
                elif arr2[self.king_x-1][self.king_y][0] == 'w':
                    ind = 0
                    # os.system('aplay ./sound1.mp3&2>/dev/null')
                    if len(arr2[self.king_x-1][self.king_y]) == 6:
                        ind = int(10*int(arr2[self.king_x-1][self.king_y][4]) + int(arr2[self.king_x-1][self.king_y][5])) - 1
                    else:
                        ind = int(arr2[self.king_x-1][self.king_y][4])-1
                    # print(ind)
                    walls[ind].health -= self.king_power
                elif arr2[self.king_x-1][self.king_y][0] == 'c':
                    ind = int(arr2[self.king_x-1][self.king_y][6])-1
                    # os.system('aplay ./sound1.mp3&2>/dev/null')
                    cannons[ind].health -= self.king_power
                elif arr2[self.king_x-1][self.king_y][0] == 'x':
                    ind = int(arr2[self.king_x-1][self.king_y][6])-1
                # os.system('aplay ./sound1.mp3&2>/dev/null')
                    wizards[ind].health -= self.king_power
                
                elif arr2[self.king_x-1][self.king_y][0] == 'h':
                    ind = int(arr2[self.king_x-1][self.king_y][3])-1
                    # os.system('aplay ./sound1.mp3&2>/dev/null')
                    huts[ind].health -= self.king_power
            elif arr2[self.king_x+1][self.king_y] != ' ':
                if arr2[self.king_x+1][self.king_y][0] == 't':
                    townhall.health -= self.king_power
                    # os.system('aplay ./sound1.mp3&2>/dev/null')
                elif arr2[self.king_x+1][self.king_y][0] == 'w':
                    ind = 0
                    # os.system('aplay ./sound1.mp3&2>/dev/null')
                    if len(arr2[self.king_x+1][self.king_y]) == 6:
                        ind = int(10*int(arr2[self.king_x+1][self.king_y][4]) + int(arr2[self.king_x+1][self.king_y][5])) - 1
                    else:
                        ind = int(arr2[self.king_x+1][self.king_y][4])-1
                    # print(ind)
                    walls[ind].health -= self.king_power
                elif arr2[self.king_x+1][self.king_y][0] == 'c':
                    ind = int(arr2[self.king_x+1][self.king_y][6])-1
                    # os.system('aplay ./sound1.mp3&2>/dev/null')
                    cannons[ind].health -= self.king_power
                elif arr2[self.king_x+1][self.king_y][0] == 'h':
                    ind = int(arr2[self.king_x+1][self.king_y][3])-1
                    huts[ind].health -= self.king_power
                    # os.system('aplay ./sound1.mp3&2>/dev/null')
            
        else:
            if last_direction == "w":
                    positions = [-8,0] 
            elif last_direction == "s":
                positions = [8,0]
            elif last_direction == "a":
                positions = [0,-8]
            elif last_direction == "d":
                positions = [0,8]
            direction = []
            for i in range(5):
                    for j in range(5):
                        direction.append([positions[0]+i-2,positions[1]+j-2])
            for i in range(len(direction)):
                if self.king_x + direction[i][0] >= 0 and self.king_x + direction[i][0] < rows and self.king_x + direction[i][1] >= 0 and self.king_x + direction[i][1] < cols:
                    colr[self.king_x+direction[i][0]][self.king_y+direction[i][1]] = "BLUE"
                    if arr2[self.king_x+direction[i][0]][self.king_y+direction[i][1]] != ' ':
                        if arr2[self.king_x+direction[i][0]][self.king_y+direction[i][1]][0] == 't':
                            townhall.health -= self.king_power
                            # os.system('aplay ./sound1.mp3&2>/dev/null')
                        elif arr2[self.king_x+direction[i][0]][self.king_y+direction[i][1]][0] == 'w':
                            #print(arr[2])
                            # os.system('aplay ./sound1.mp3&2>/dev/null')
                            ind = 0
                            if len(arr2[self.king_x+direction[i][0]][self.king_y+direction[i][1]]) == 6:
                                ind = int(10*int(arr2[self.king_x+direction[i][0]][self.king_y+direction[i][1]][4]) + int(arr2[self.king_x+direction[i][0]][self.king_y+direction[i][1]][5])) - 1
                            else:
                                ind = int(arr2[self.king_x+direction[i][0]][self.king_y+direction[i][1]][4])-1
                            # print(ind)
                            walls[ind].health -= self.king_power
                        elif arr2[self.king_x+direction[i][0]][self.king_y+direction[i][1]][0] == 'c':
                            ind = int(arr2[self.king_x+direction[i][0]][self.king_y+direction[i][1]][6])-1
                            cannons[ind].health -= self.king_power
                            # os.system('aplay ./sound1.mp3&2>/dev/null')
                        elif arr2[self.king_x+direction[i][0]][self.king_y+direction[i][1]][0] == 'x':
                            ind = int(arr2[self.king_x+direction[i][0]][self.king_y+direction[i][1]][6])-1
                            wizards[ind].health -= self.king_power
                            # os.system('aplay ./sound1.mp3&2>/dev/null')
                        elif arr2[self.king_x+direction[i][0]][self.king_y+direction[i][1]][0] == 'h':
                            ind = int(arr2[self.king_x+direction[i][0]][self.king_y+direction[i][1]][3])-1
                            huts[ind].health -= self.king_power
                            # os.system('aplay ./sound1.mp3&2>/dev/null')
