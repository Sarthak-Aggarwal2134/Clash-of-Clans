from colorama import Fore, Back, Style

rows=15
cols=100


ar=[[rows]*cols for i in range(rows)]
every_troop = []
every_ground_troop=[]
every_building = []
for i in range(rows):
    for j in range(cols):
        ar[i][j] = ' '

#ar[14][28]=ar[14][29]=ar[14][30]=ar[14][31]=ar[14][32]="T"
#ar[15][28]=ar[15][29]=ar[15][30]=ar[15][31]=ar[15][32]="T"
#ar[16][28]=ar[16][29]=ar[16][30]=ar[16][31]=ar[16][32]="T"

#ar[21][44]=ar[21][45]=ar[21][46]="B"
#ar[22][44]=ar[22][45]=ar[22][46]="B"


#ar[21][14]=ar[21][15]=ar[21][16]="B"
#ar[22][14]=ar[22][15]=ar[22][16]="B"

#ar[6][44]=ar[6][45]=ar[6][46]="B"
#ar[7][44]=ar[7][45]=ar[7][46]="B"

#ar[6][14]=ar[6][15]=ar[6][16]="B"
#ar[7][14]=ar[7][15]=ar[7][16]="B"


total_buildings=13
#making border

arr2=[[rows]*cols for i in range(rows)]
for i in range(rows):
    for j in range(cols):
        arr2[i][j] = ' '

colr=[[rows]*cols for i in range(rows)]
for i in range(rows):
    for j in range(cols):
        colr[i][j] = ' '

for i in range(rows):
    for j in range(cols):
        if i==0 and j==46:
            ar[i][j]='2'
        elif i==6 and j==0:
            ar[i][j]='1'
        elif i== 4 and j== 99:
            ar[i][j]='3'
        elif i==12 and j==0:
            ar[i][j]='4'
        elif i==10 and j==99:
            ar[i][j]='5'
        elif i==0 and j==89:
            ar[i][j]='6'
        elif i==8 and j==0:
            ar[i][j]='7'
        elif i==12 and j==99:
            ar[i][j]='8'
        elif i==0 and j==69:
            ar[i][j]='9'    
        elif (j==0) or ( j==cols-1):
            ar[i][j]="|"
            arr2[i][j]="|"
        elif i==0 or i==rows-1:
            ar[i][j] = '-'
            arr2[i][j]= '-'
           
