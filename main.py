from initial import Initial
from buildings import *
from king import *
import os
from input import *
from sceneery import *
from spell import spell
from troops import *
import os.path

level_1_barbs=5
level_1_archers=5
level_1_balloons=5

level_2_barbs=7
level_2_archers=7
level_2_balloons=7


level_3_barbs=10
level_3_archers=10
level_3_balloons=10


level_1=False
level_2=False
level_3=False

count_barbs=0
count_archers=0
count_balloons=0


prev_build=13
os.system('clear')
game = Initial()
lol =[]
lol1=['T' for k in range(15)]
townhall=building('townhall',7,40,lol,lol1)
xd=[]
xd2 = []
huts = []
can=[]
can2=['C' for k in range(2)]
wall=[]
wiz=[]
cannons = []
level = 1
wizards = []
wiz2=['X' for k in range(2)]
wall2=['#' for k in range(1)]
walls = []
king_pos = [5,5]
king = kings('King',king_pos[0],king_pos[1])

def init_game():
    global lol
    lol.clear()
    for i in range(3):
        for j in range(5):
            lol.append([i,j])
    # lol=[i,j]6
    townhall.health=500
    every_building.clear()
    every_building.append(townhall)
    king.king_health=100
    townhall.print_building()
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

    global level_1 
    level_1=True
    # king.build()
    # avatar="q"
    last_direction="d"
    # lol=level
    xd.clear()
    for i in range(2):
        for j in range(4):
            xd.append([i,j])
    xd2.clear()
    for k in range(8):
        xd2.append('H') 
    # xd2=['H' for k in range(8)]
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
    global count_barbs
    global count_archers
    global count_balloons
    count_barbs=0
    count_archers=0
    count_balloons=0
    # [hut1,hut2,hut3,hut4,hut5]
    huts.clear()
    huts.append(hut1)
    huts.append(hut2)
    huts.append(hut3)
    huts.append(hut4)
    huts.append(hut5)
    every_building.append(hut1)
    every_building.append(hut2)
    every_building.append(hut3)
    every_building.append(hut4)
    every_building.append(hut5)
    
    for i in range(1):
        for j in range(2):
            can.append([i,j])

    cannons.clear()
    cannon1=Cannon('cannon1',2,30,can,can2)
    cannon1.print_building()
    cannon2=Cannon('cannon2',2,50,can,can2)
    cannon2.print_building()
    cannon3=Cannon('cannon3',12,30,can,can2)
    cannon3.print_building()
    cannon4=Cannon('cannon4',12,50,can,can2)
    cannon4.print_building()
    cannon5=Cannon('cannon5',8,60,can,can2)
    cannon5.print_building()

    
    for i in range(1):
        for j in range(2):
            wiz.append([i,j])

    wizards.clear()
    wizard1=Cannon('xizard1',2,40,wiz,wiz2)
    wizard1.print_building()
    wizard2=Cannon('xizard2',12,40,wiz,wiz2)
    wizard2.print_building()
    cannons.append(cannon1)
    cannons.append(cannon2)
    cannons.append(cannon3)
    cannons.append(cannon4)
    cannons.append(cannon5)
    wizards.append(wizard1)
    wizards.append(wizard2)
    every_building.append(cannon1)
    every_building.append(cannon2)
    every_building.append(cannon3)
    every_building.append(cannon4)
    every_building.append(cannon5)
    every_building.append(wizard1)
    every_building.append(wizard2)
    # [cannon1,cannon2,cannon3,cannon4,cannon5]
    # [wizard1,wizard2]

    

    for i in range(1):
        for j in range(1):
            wall.append([i,j])

    

    
    # [wall_num1,wall_num2,wall_num3,wall_num4,wall_num5,wall_num6,wall_num7,wall_num8,wall_num9,wall_num10,wall_num11,wall_num12,wall_num13,wall_num14,wall_num15,wall_num16,wall_num17,wall_num18,wall_num19,wall_num20,wall_num21,wall_num22,wall_num23,wall_num24,wall_num25,wall_num26,wall_num27,wall_num28,wall_num29]
    walls.append(wall_num1)
    walls.append(wall_num2)
    walls.append(wall_num3)
    walls.append(wall_num4)
    walls.append(wall_num5)
    walls.append(wall_num6)
    walls.append(wall_num7)
    walls.append(wall_num8)
    walls.append(wall_num9)
    walls.append(wall_num10)
    walls.append(wall_num11)
    walls.append(wall_num12)
    walls.append(wall_num13)
    walls.append(wall_num14)
    walls.append(wall_num15)
    walls.append(wall_num16)
    walls.append(wall_num17)
    walls.append(wall_num18)
    walls.append(wall_num19)
    walls.append(wall_num20)
    walls.append(wall_num21)
    walls.append(wall_num22)
    walls.append(wall_num23)
    walls.append(wall_num24)
    walls.append(wall_num25)
    walls.append(wall_num26)
    walls.append(wall_num27)
    walls.append(wall_num28)
    walls.append(wall_num29)



    # king_pos = [5,5]
    townhall.build()
    king.build()
    for i in cannons:
        i.build()
    for i in huts:
        i.build()
    for i in walls:
        i.build()
    for i in wizards:
        i.build()

    prev_build=13


# if level==2:
    #     cannon6=Cannon('cannon6',2,60,can,can2)
    #     cannon6.print_building()
    #     wizard3=Cannon('xizard3',2,80,wiz,wiz2)
    #     wizard3.print_building()
    #     cannons=[cannon1,cannon2,cannon3,cannon4,cannon5,cannon6]
    #     wizards=[wizard1,wizard2,wizard3]
    # elif level==3:
    #     cannon6=Cannon('cannon6',2,60,can,can2)
    #     cannon6.print_building()
    #     cannon7=Cannon('cannon7',2,80,can,can2)
    #     cannon7.print_building()
    #     wizard3=Cannon('xizard3',2,80,wiz,wiz2)
    #     wizard3.print_building()
    #     wizard4=Cannon('xizard4',12,80,wiz,wiz2)
    #     wizard4.print_building()
    #     cannons=[cannon1,cannon2,cannon3,cannon4,cannon5,cannon6,cannon7]
    #     wizards=[wizard1,wizard2,wizard3,wizard4]

def Second():
    for i in every_troop:
        ar[i.x][i.y] = " "
        every_troop.remove(i)
    for i in every_ground_troop:
        ar[i.x][i.y] = " "
        every_ground_troop.remove(i)
    ar[king.king_x][king.king_y] = " "
    king.king_x = 5
    king.king_y = 5
    global level_1
    global level_2
    level_2=True
    init_game()
    level_1=False   
    global count_barbs
    global count_archers
    global count_balloons
    count_barbs=0
    count_archers=0
    count_balloons=0
    global cannons,wizards
    cannon6=Cannon('cannon6',2,60,can,can2)
    cannon6.print_building()
    wizard3=Cannon('xizard3',2,80,wiz,wiz2)
    wizard3.print_building()
    cannons.append(cannon6)
    wizards.append(wizard3)
    every_building.append(cannon6)
    every_building.append(wizard3)
    prev_build=15

def Third():
    for i in every_troop:
        ar[i.x][i.y] = " "
        every_troop.remove(i)
    for i in every_ground_troop:
        ar[i.x][i.y] = " "
        every_ground_troop.remove(i)
    ar[king.king_x][king.king_y] = " "
    king.king_x = 5
    king.king_y = 5
    global level_2
    global level_3
    global level_1
    level_2=False
    level_3=True
    init_game()
    global cannons,wizards
    level_1=False
    global count_barbs
    global count_archers
    global count_balloons
    count_barbs=0
    count_archers=0
    count_balloons=0
    cannon6=Cannon('cannon6',2,60,can,can2)
    cannon6.print_building()
    cannon7=Cannon('cannon7',2,80,can,can2)
    cannon7.print_building()
    wizard3=Cannon('xizard3',2,80,wiz,wiz2)
    wizard3.print_building()
    wizard4=Cannon('xizard4',12,80,wiz,wiz2)
    wizard4.print_building()
    cannons.append(cannon6)
    cannons.append(cannon7)
    wizards.append(wizard3)
    wizards.append(wizard4)
    every_building.append(cannon6)
    every_building.append(wizard3)
    every_building.append(cannon7)
    every_building.append(wizard4)
    prev_build=17

# for i in range(1000):
#     if os.path.exists('replays/replay' + str(i)+'.txt'):\
#         continue
#     else:
#         file1 = open("replays/replay" + str(i)+".txt", "a")  # append mode
#         break

print("Choose Avatar: Press k for king and q for queen")
f =  Get()
avt = Get.__call__(f)
avatar = avt
init_game()
while True:

    os.system('clear')
    if townhall.health<=0:
        townhall.build()
        total_buildings-=1
        if townhall in every_building:
            every_building.remove(townhall)
    for i in cannons:
        i.build()
        if i.health<=0:
            total_buildings-=1
            prev_build-=1
            if i in every_building:
                every_building.remove(i)
    for i in walls:
        i.build()
    for i in every_troop:
        
        i.move(every_building)
    
    for i in huts:
        i.build()
        if i.health<=0:
            total_buildings-=1
            prev_build-=1
            if i in every_building:
                every_building.remove(i)
    for i in wizards:
        i.build()
        if i.health<=0:
            total_buildings-=1
            prev_build-=1
            if i in every_building:
                every_building.remove(i)
    king.build()
    troops_health = 0
    for i in every_troop:
        troops_health+=i.health
    if len(every_building)==0 and level == 1:
        level += 1
        print("Next level")
        Second()
    elif len(every_building)==0 and level == 2:
        level += 1
        print("Next level")
        Third()
    elif len(every_building)==0 and level == 3:
        print("You Won")
        break
    elif king.king_health<=0 and troops_health == 0:
        print("You lose!")
        break
    # else:
    #     print("You win!")
    #     level+=1
    
    x=scene()
    scene.print_grid(x,townhall,walls,cannons,huts,king,wizards,avatar)
    print("TOTAL BUILDINGS: ",len(every_building))
    print(level_1,level_2,level_3)
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
        # i.print_building()
    # print(arr2)
    g = Get()
    ch = input_to(g)
    if ch == 'a' or ch=='w' or ch=='s' or ch=='d':
        last_direction=ch
        # file1.write(ch + "\n")
        king.move(ch)
    elif ch==' ':
        # file1.write(ch + "\n")
        king.attack(townhall,huts,cannons,walls,wizards,avatar,last_direction)
    elif ch=='1' or ch=='2' or ch=='3':
        if level_1==True:
            if count_barbs<=level_1_barbs:
        # file1.write(ch + "\n")
                T = barbs()
                T.gen(ch)
                every_troop.append(T)
                every_ground_troop.append(T)
                count_barbs+=1
        elif level_2==True:
            if count_barbs<=level_2_barbs:
            # file1.write(ch + "\n")
                T = barbs()
                T.gen(ch)
                every_troop.append(T)
                every_ground_troop.append(T)
                count_barbs+=1
        elif level_3==True:
            if count_barbs<=level_3_barbs:
            # file1.write(ch + "\n")
                T = barbs()
                T.gen(ch)
                every_troop.append(T)
                every_ground_troop.append(T)
                count_barbs+=1
    elif ch=='4' or ch=='5' or ch=='6':
        if level_1:
            if count_archers<=level_1_archers:
        # file1.write(ch + "\n")
                T = archer()
                T.gen(ch)
                every_troop.append(T)
                every_ground_troop.append(T)
                count_archers+=1
        elif level_2:
            if count_archers<=level_2_archers:
            # file1.write(ch + "\n")
                T = archer()
                T.gen(ch)
                every_troop.append(T)
                every_ground_troop.append(T)
                count_archers+=1
        elif level_3:
            if count_archers<=level_3_archers:
            # file1.write(ch + "\n")
                T = archer()
                T.gen(ch)
                every_troop.append(T)
                every_ground_troop.append(T)
                count_archers+=1
        # file1.write(ch + "\n")
    elif ch=='7' or ch=='8' or ch=='9':
        if level_1:
            if count_balloons<=level_1_balloons:
        # file1.write(ch + "\n")
                T = balloons()
                T.gen(ch)
                every_troop.append(T)
                count_balloons+=1
        elif level_2:
            if count_balloons<=level_2_balloons:
            # file1.write(ch + "\n")
                T = balloons()
                T.gen(ch)
                every_troop.append(T)
                count_balloons+=1
        elif level_3:
            if count_balloons<=level_3_balloons:
            # file1.write(ch + "\n")
                T = balloons()
                T.gen(ch)
                every_troop.append(T)
                count_balloons+=1
        # file1.write(ch + "\n")
        # T = balloons()
        # T.gen(ch)
        # every_troop.append(T)
    elif ch=='h' or ch=='r':
        s = spell(ch,king,every_troop)
        # s.drop(ch)
    elif ch=='q':
        break
        # file1.close()
    # else:
    #     file1.write('|\n')
    townhall.build()
    
    for i in every_troop:
        if i.health<=0:
            ar[i.x][i.y]=' '
            every_troop.remove(i)
        else:
            i.move(every_building)

    for i in cannons:
        if i.health>0:
            x=abs(i.top_r_x-king.king_x)
            y=abs(i.top_r_y-king.king_y)
            if x+y<4:
                king.king_health-=2
                i.active=True
            else:
                i.active=False
            for j in every_ground_troop:
                if i.active == False:
                    x = abs(i.top_r_x-j.x)
                    y = abs(i.top_r_y-j.y)
                    if x+y<4 and j.health>0:
                        j.health-=2
                        i.active=True
                    else:
                        i.active=False
                else: 
                    break
        else:
            i.active=False


    for i in wizards:
        if i.health>0:
            x=abs(i.top_r_x-king.king_x)
            y=abs(i.top_r_y-king.king_y)
            if x+y<4:
                king.king_health-=2
                i.active=True
            else:
                i.active=False
            for j in every_troop:
                if i.active == False:
                    x = abs(i.top_r_x-j.x)
                    y = abs(i.top_r_y-j.y)
                    if x+y<4 and j.health>0:
                        j.health-=2
                        i.active=True
                    else:
                        i.active=False
                else: 
                    break
        else:
            i.active=False
    king.build()

    

