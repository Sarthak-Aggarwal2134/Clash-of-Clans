from initial import Initial
from buildings import *
from king import kings
import os
from input import *
from sceneery import *
from spell import spell
from troops import *

os.system('clear')
game = Initial()
lol =[]
for i in range(3):
    for j in range(5):
        lol.append([i,j])
# lol=[i,j]6
lol1=['T' for k in range(15)]
townhall=building('townhall',7,40,lol,lol1)
townhall.print_building()
xd=[]

for i in range(2):
    for j in range(4):
        xd.append([i,j])

xd2=['H' for k in range(8)]
hut1=building('hut1',2,20,xd,xd2)
hut1.print_building()
hut2=building('hut2',12,20,xd,xd2)
hut2.print_building()
hut3=building('hut3',2,70,xd,xd2)
hut4=building('hut4',12,70,xd,xd2)
hut5=building('hut5',6,75,xd,xd2)
hut3.print_building()
hut4.print_building()
hut5.print_building()
huts = [hut1,hut2,hut3,hut4,hut5]
can=[]
for i in range(1):
    for j in range(2):
        can.append([i,j])

can2=['C' for k in range(2)]
cannon1=building('cannon1',2,30,can,can2)
cannon1.print_building()
cannon2=building('cannon2',2,50,can,can2)
cannon2.print_building()
cannon3=building('cannon3',12,30,can,can2)
cannon3.print_building()
cannon4=building('cannon4',12,50,can,can2)
cannon4.print_building()
cannon5=building('cannon5',8,60,can,can2)
cannon5.print_building()
cannons = [cannon1,cannon2,cannon3,cannon4,cannon5]
wall=[]

for i in range(1):
    for j in range(1):
        wall.append([i,j])

wall2=['#' for k in range(1)]

wall_num1=building('wall1',5,38,wall,wall2)
wall_num1.print_building()
wall_num2=building('wall2',5,39,wall,wall2)
wall_num2.print_building()
wall_num3=building('wall3',5,40,wall,wall2)
wall_num3.print_building()
wall_num4=building('wall4',5,41,wall,wall2)
wall_num4.print_building()
wall_num5=building('wall5',5,42,wall,wall2)
wall_num5.print_building()
wall_num6=building('wall6',5,43,wall,wall2)
wall_num6.print_building()
wall_num7=building('wall7',5,44,wall,wall2)
wall_num7.print_building()
wall_num8=building('wall8',5,45,wall,wall2)
wall_num8.print_building()
wall_num9=building('wall9',5,46,wall,wall2)
wall_num9.print_building()

wall_num10=building('wall10',6,46,wall,wall2)
wall_num10.print_building()
wall_num11=building('wall11',7,46,wall,wall2)
wall_num11.print_building()
wall_num12=building('wall12',8,46,wall,wall2)
wall_num12.print_building()
wall_num13=building('wall13',9,46,wall,wall2)
wall_num13.print_building()
wall_num14=building('wall14',10,46,wall,wall2)
wall_num14.print_building()
wall_num15=building('wall15',11,46,wall,wall2)
wall_num15.print_building()
wall_num16=building('wall16',5,38,wall,wall2)
wall_num16.print_building()
wall_num17=building('wall17',6,38,wall,wall2)
wall_num17.print_building()
wall_num18=building('wall18',7,38,wall,wall2)
wall_num18.print_building()
wall_num19=building('wall19',8,38,wall,wall2)
wall_num19.print_building()
wall_num20=building('wall20',9,38,wall,wall2)
wall_num20.print_building()
wall_num21=building('wall21',10,38,wall,wall2)
wall_num21.print_building()
wall_num22=building('wall22',11,38,wall,wall2)

wall_num22.print_building()
wall_num23=building('wall23',11,39,wall,wall2)
wall_num23.print_building()
wall_num24=building('wall24',11,40,wall,wall2)
wall_num24.print_building()
wall_num25=building('wall25',11,41,wall,wall2)
wall_num25.print_building()
wall_num26=building('wall26',11,42,wall,wall2)
wall_num26.print_building()
wall_num27=building('wall27',11,43,wall,wall2)
wall_num27.print_building()
wall_num28=building('wall28',11,44,wall,wall2)
wall_num28.print_building()
wall_num29=building('wall29',11,45,wall,wall2)
wall_num29.print_building()
walls = [wall_num1,wall_num2,wall_num3,wall_num4,wall_num5,wall_num6,wall_num7,wall_num8,wall_num9,wall_num10,wall_num11,wall_num12,wall_num13,wall_num14,wall_num15,wall_num16,wall_num17,wall_num18,wall_num19,wall_num20,wall_num21,wall_num22,wall_num23,wall_num24,wall_num25,wall_num26,wall_num27,wall_num28,wall_num29]
king = kings('King',5,5)
townhall.build()
king.build()
for i in cannons:
    i.build()
for i in huts:
    i.build()
for i in walls:
    i.build()


file = open(f"replays/{sys.argv[1]}", "r")
lines = file.readlines()
for line in lines:
    
    os.system('clear')
    if townhall.health<=0:
        total_buildings-=1
    for i in cannons:
        i.build()
        
        if i.health<=0:
            total_buildings-=1
    for i in huts:
        i.build()
        if i.health<=0:
            total_buildings-=1
    
    if total_buildings!=0:
        total_buildings=11
    else:
        if king.king_health<=0:
            print("You lose!")
            break
        else:
            print("You win!")
        break
    
    x=scene()
    scene.print_grid(x,townhall,walls,cannons,huts,king)

    # for i in range(rows):
    #     for j in range(cols):
    #         if ar[i][j]=='T':
    #             arr2[i][j]='townhall'
    #         elif ar[i][j]=='C':
    #             arr2[i][j]='cannon'
    #         elif ar[i][j]=='H':
    #             arr2[i][j]='hut'
    #         elif ar[i][j]=='#':
    #             arr2[i][j]='wall'
    #     i.print_building()
    # print(arr2)
    g = Get()
    sarthak = input_to(g)
    ch = line[0]

    
    if ch == 'a' or ch=='w' or ch=='s' or ch=='d':
    #     
        king.move(ch)
    elif ch==' ':
        king.attack(townhall,huts,cannons,walls)
    
    elif ch=='1' or ch=='2' or ch=='3':
        T = troops()
        T.gen(ch)
        every_troop.append(T)
    elif ch=='h' or ch=='r':
        s = spell(ch,king,every_troop)
        # s.drop(ch)
    elif ch=='q':
        break
    townhall.build()
    for i in every_troop:
        i.move(every_building)
        if i.health<=0:
            every_troop.remove(i)
    for i in cannons:
        if i.health>0:
            x=abs(i.top_r_x-king.king_x)
            y=abs(i.top_r_y-king.king_y)
            if x+y<4:
                king.king_health-=2
                i.active=True
            else:
                i.active=False
        else:
            i.active=False
    
    for i in walls:
        i.build()
    king.build()
    

