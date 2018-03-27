# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 15:46:16 2018

@author: Pedro
"""
#Lists of objects
food = ["beans","bar","meat"]
locations = ["forrest","cabin","cave","mountain","river basin","beach"]
options = ["north", "south", "east", "west"]
environments = ["forrest_env","cabin_env","cave_env","mountain_env","river basin_env","beach_env"]
good_animals = ["rabbit","bird","bug"]
bad_animals = ["wolf","poisonous snake"]
health_status = ["Healthy","Injured","Poisoned"]
food_status = ["Full","Hungry","Starving"]
drink_status = ["Full","Thristy","Dehydrating"]

locations_dic = {"forrest": "forrest_env",
                 "cabin":"cabin_env",
                 "cave": "cave_env",
                 "mountain": "mountain_env",
                 "river basin": "river_basin_env",
                 "beach": "beach_env"}


#Modules needed
import time
import random

#Current possition
c_pos = str(random.choice(locations))

#Start game
print ("After a long walk you got lost in a " + str(c_pos) + ".\nTry to survive and find your way back")

#Setting the location environment (in development)
#print (str(locations_dic[c_pos]))

time.sleep(5)

#Number of turns
turns=1000
ap = 1

#Turn base loop
time.sleep (1)
while turns > 0:
    print ("NEW TURN")
    time.sleep (1)
    choice = input ("You have " + str(ap) + " action points.\nWhat you want to do?(walk / actions)\nR:")
    #Base walking loop
    if choice == "walk":
        path = input ("Which way you want to go (north, south, east, west) \nR:")
        if path == "north":
                print ("Walking.")
                time.sleep(1)
                print ("Walking..")
                time.sleep(1)
                print ("Walking...")
                time.sleep(1)
                turns -= 1
                break
    if path == "break":
        break
    else:
        print ("I've waisted my time")
        
    #Base actions loop
    if ap > 0:
        print

    
    
    
    
    
    
    
    
    