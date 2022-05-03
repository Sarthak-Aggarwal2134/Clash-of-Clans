from buildings import *
import os
from glo_var import *
# from .main import *
class spell():
    def __init__(self,char,king,every_troop):
        self.drop(char,king,every_troop)
    def drop(self,char,king,every_troop):
        if char=='h':
            if king.king_health<=50:
                king.king_health+=50
            for i in every_troop:
                if i.health<=5:
                    i.health+=5
            
        elif char=='r':
            if king.king_speed==1:
                king.king_speed*=2
                king.king_power*=2
            for i in every_troop:
                if i.troop_speed==2:
                    i.troop_speed*=2
                    i.troop_power*=2