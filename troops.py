from re import X
from glo_var import *
from buildings import *
class barbs():
    def __init__(self):
        self.x = 0
        self.y=  0
        self.health=10
        self.attack = 2
    def gen(self,ch):
        if ch == '1':
            ar[6][1]='0'
            self.x = 6
            self.y = 1
        elif ch=='2':
            ar[1][46]='0'
            self.x = 1
            self.y = 46
        elif ch=='3':
            ar[4][98]='0'   
            self.x = 4
            self.y = 98

    def move(self,every_building):
        # ar[self.x][self.y]=' '
        max=999
        for bld in every_building:
            if bld.health>0:
                for p in bld.list1:
                    x_dist=abs(self.x-bld.top_r_x-p[0])
                    y_dist=abs(self.y-bld.top_r_y-p[1])
                    if x_dist+y_dist<max:
                        max=x_dist+y_dist
                        target_building = bld
                        target_point = [bld.top_r_x + p[0],bld.top_r_y + p[1]]
        if max != 999:
            in_cannon=False
            if max == 1 or (max == 2 and self.x!= target_point[0] and self.y != target_point[1] ):
                if arr2[target_point[0]][target_point[1]] == 'townhall':
                    target_building.health-=self.attack
                elif arr2[target_point[0]][target_point[1]]=='cannon1':
                    target_building.health-=self.attack
                    self.health=0
                    self.attack=0
                    in_cannon=True
                elif arr2[target_point[0]][target_point[1]]=='cannon2':
                    target_building.health-=self.attack
                    self.health=0
                    self.attack=0
                    in_cannon=True
                elif arr2[target_point[0]][target_point[1]]=='cannon3':
                    target_building.health-=self.attack
                    self.health=0
                    self.attack=0
                    in_cannon=True
                elif arr2[target_point[0]][target_point[1]]=='cannon4':
                    target_building.health-=self.attack
                    self.health=0
                    self.attack=0
                    in_cannon=True
                elif arr2[target_point[0]][target_point[1]]=='cannon5':
                    target_building.health-=self.attack
                    self.health=0
                    self.attack=0
                    in_cannon=True
                elif arr2[target_point[0]][target_point[1]]=='hut1':
                    target_building.health-=self.attack
                elif arr2[target_point[0]][target_point[1]]=='hut2':
                    target_building.health-=self.attack
                elif arr2[target_point[0]][target_point[1]]=='hut3':
                    target_building.health-=self.attack
                elif arr2[target_point[0]][target_point[1]]=='hut4':
                    target_building.health-=self.attack
                elif arr2[target_point[0]][target_point[1]]=='hut5':
                    target_building.health-=self.attack
                    
            else:
                if ar [self.x][self.y+1]==' ' or ar [self.x][self.y-1]==' ' or ar [self.x+1][self.y]==' ' or ar [self.x -1][self.y]==' ':
                    ar[self.x][self.y]=' '
                    arr2[self.x][self.y]=' ' 
                if self.x<target_building.top_r_x:
                    self.x+=1
                elif self.x>target_building.top_r_x:
                    self.x-=1
                if self.y<target_building.top_r_y:
                    self.y+=1
                elif self.y>target_building.top_r_y:
                    self.y-=1
                ar[self.x][self.y]='0'




class archer():
    def __init__(self):
        self.x = 0
        self.y=  0
        self.health=10
        self.attack = 2
    def gen(self,ch):
        if ch=='4':
            ar[12][1]='*'   
            self.x = 12
            self.y = 1
        elif ch=='5':
            ar[10][98]='*'   
            self.x = 10
            self.y = 98
        elif ch=='6':
            ar[1][89]='*'   
            self.x = 1
            self.y = 89

    def move(self,every_building):
        # ar[self.x][self.y]=' '
        max=999
        for bld in every_building:
            if bld.health>0:
                for p in bld.list1:
                    x_dist=abs(self.x-bld.top_r_x-p[0])
                    y_dist=abs(self.y-bld.top_r_y-p[1])
                    if x_dist+y_dist<max:
                        max=x_dist+y_dist
                        target_building = bld
                        target_point = [bld.top_r_x + p[0],bld.top_r_y + p[1]]
        if max != 999:
            in_cannon=False
            if max <= 4:
                if arr2[target_point[0]][target_point[1]] == 'townhall':
                    target_building.health-=self.attack
                elif arr2[target_point[0]][target_point[1]]=='cannon1':
                    target_building.health-=self.attack
                    self.health=0
                    self.attack=0
                    in_cannon=True
                elif arr2[target_point[0]][target_point[1]]=='cannon2':
                    target_building.health-=self.attack
                    self.health=0
                    self.attack=0
                    in_cannon=True
                elif arr2[target_point[0]][target_point[1]]=='cannon3':
                    target_building.health-=self.attack
                    self.health=0
                    self.attack=0
                    in_cannon=True
                elif arr2[target_point[0]][target_point[1]]=='cannon4':
                    target_building.health-=self.attack
                    self.health=0
                    self.attack=0
                    in_cannon=True
                elif arr2[target_point[0]][target_point[1]]=='cannon5':
                    target_building.health-=self.attack
                    self.health=0
                    self.attack=0
                    in_cannon=True
                elif arr2[target_point[0]][target_point[1]]=='hut1':
                    target_building.health-=self.attack
                elif arr2[target_point[0]][target_point[1]]=='hut2':
                    target_building.health-=self.attack
                elif arr2[target_point[0]][target_point[1]]=='hut3':
                    target_building.health-=self.attack
                elif arr2[target_point[0]][target_point[1]]=='hut4':
                    target_building.health-=self.attack
                elif arr2[target_point[0]][target_point[1]]=='hut5':
                    target_building.health-=self.attack
                    
            else:
                if ar [self.x][self.y+1]==' ' or ar [self.x][self.y-1]==' ' or ar [self.x+1][self.y]==' ' or ar [self.x -1][self.y]==' ':
                    ar[self.x][self.y]=' '
                    arr2[self.x][self.y]=' ' 
                if self.x<target_building.top_r_x:
                    self.x+=1
                elif self.x>target_building.top_r_x:
                    self.x-=1
                if self.y<target_building.top_r_y:
                    self.y+=1
                elif self.y>target_building.top_r_y:
                    self.y-=1
                ar[self.x][self.y]='*'




class balloons():
    def __init__(self):
        self.x = 0
        self.y=  0
        self.health=10
        self.attack = 2
    def gen(self,ch):
        if ch=='7':
            ar[8][1]='+'   
            self.x = 8
            self.y = 1
        elif ch=='8':
            ar[12][98]='+'   
            self.x = 12
            self.y = 98
        elif ch=='9':
            ar[1][69]='+'   
            self.x = 1
            self.y = 69

    def move(self,every_building):
        # ar[self.x][self.y]=' '
        max=999
        for bld in every_building:
            if bld.health>0:
                for p in bld.list1:
                    x_dist=abs(self.x-bld.top_r_x-p[0])
                    y_dist=abs(self.y-bld.top_r_y-p[1])
                    if x_dist+y_dist<max:
                        max=x_dist+y_dist
                        target_building = bld
                        target_point = [bld.top_r_x + p[0],bld.top_r_y + p[1]]
        if max != 999:
            # in_cannon=False
            if max == 1 or (max == 2 and self.x!= target_point[0] and self.y != target_point[1] ):
                if arr2[target_point[0]][target_point[1]] == 'townhall':
                    target_building.health-=self.attack
                elif arr2[target_point[0]][target_point[1]]=='cannon1':
                    target_building.health-=self.attack
                    # in_cannon=True
                elif arr2[target_point[0]][target_point[1]]=='cannon2':
                    target_building.health-=self.attack
                    
                    # in_cannon=True
                elif arr2[target_point[0]][target_point[1]]=='cannon3':
                    target_building.health-=self.attack
                    
                    # in_cannon=True
                elif arr2[target_point[0]][target_point[1]]=='cannon4':
                    target_building.health-=self.attack
                    
                    # in_cannon=True
                elif arr2[target_point[0]][target_point[1]]=='cannon5':
                    target_building.health-=self.attack
                    
                    # in_cannon=True
                elif arr2[target_point[0]][target_point[1]]=='hut1':
                    target_building.health-=self.attack
                elif arr2[target_point[0]][target_point[1]]=='hut2':
                    target_building.health-=self.attack
                elif arr2[target_point[0]][target_point[1]]=='hut3':
                    target_building.health-=self.attack
                elif arr2[target_point[0]][target_point[1]]=='hut4':
                    target_building.health-=self.attack
                elif arr2[target_point[0]][target_point[1]]=='hut5':
                    target_building.health-=self.attack
                    
            else:
                if ar [self.x][self.y+1]==' ' or ar [self.x][self.y-1]==' ' or ar [self.x+1][self.y]==' ' or ar [self.x -1][self.y]==' ':
                    ar[self.x][self.y]=' '
                    arr2[self.x][self.y]=' ' 
                if self.x<target_building.top_r_x:
                    self.x+=1
                elif self.x>target_building.top_r_x:
                    self.x-=1
                if self.y<target_building.top_r_y:
                    self.y+=1
                elif self.y>target_building.top_r_y:
                    self.y-=1
                ar[self.x][self.y]='+'