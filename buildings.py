from distutils.command.build import build
from glo_var import *
from king import *
class building():
    def __init__(self,name,top_r_x,top_r_y,list1,list2):
        self.name=name
        self.top_r_x=top_r_x
        self.top_r_y=top_r_y
        self.list1=list1
        self.list2=list2
        self.health = 100
        self.active=False
        if self.name == "townhall":
            self.health = 500
            arr2[self.top_r_x][self.top_r_y]=self.name
        elif self.name[0] == 'w':
            self.health = 1
            arr2[self.top_r_x][self.top_r_y]=self.name
        elif self.name[0]=='c':
            self.health = 50
            arr2[self.top_r_x][self.top_r_y]=self.name
        elif self.name[0]=='h':
            self.health = 50
            arr2[self.top_r_x][self.top_r_y]=self.name
        elif self.name[0]=='x':
            self.health=50
            arr2[self.top_r_x][self.top_r_y]=self.name
        #if self.name[0] != 'w':
            #every_building.append(self)


    def build(self):
        if self.health<=0:
            for i in self.list1:
                ar[self.top_r_x+ i[0]] [self.top_r_y+ i[1]] = ' '
                arr2[self.top_r_x+ i[0]] [self.top_r_y+ i[1]] = ' '
        else:
            ind = 0
            for i in self.list1:
                ar[self.top_r_x+ i[0]] [self.top_r_y+ i[1]] = self.list2[ind]
                arr2[self.top_r_x+ i[0]] [self.top_r_y+ i[1]] = self.name
                # ind+=1
            
    def print_building(self):
        index=0
        for i in self.list1:
            # print(self.top_r_x + self.list1[index][0],self.top_r_y + self.list1[index][1])
            # print(self.top_r_x+ i[0])
            # print(self.top_r_y+ i[1])
            # print("index" + str(index))
            ar[self.top_r_x+ i[0]] [self.top_r_y+ i[1]] = self.list2[index]
            arr2[self.top_r_x+ i[0]] [self.top_r_y+ i[1]] = self.name
            # index+=1
        

class Cannon(building):
    def cannon_shoot(self,king):
        for i in range(rows):
            for j in range(cols):
                if ar[i][j]=='C':
                    if i-king.king_x<4:
                        king.king_health-=10
                        


            








#make border
#2d array of copy of board

#list1 mien i,j jahan T pprint krna hai
#list2 mein total T ki value pdi hai