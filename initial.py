from sceneery import scene
from colorama import Fore, Back, Style
from glo_var import *
from buildings import *

class Initial:
    def run(self,townhall,walls,cannons,huts,king):
        x=scene()
        scene.print_grid(x,townhall,walls,cannons,huts,king,avatar="k")

    
    # def print_start_vil(arr):
    #     for i in range(rows):
    #         for j in range(cols):
    #             print(ar[i][j])
    #         if townhall.health>500:




# i=3
# j=5
