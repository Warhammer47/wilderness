# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 15:46:16 2018

@author: Pedro
"""
#Lists of objects
food = ["beans","bar","meat"]
directions_options = {"north", "south", "east", "west"}
good_animals = ["rabbit","bird","bug"]
bad_animals = ["wolf","poisonous snake"]
health_status = ["Healthy","Injured","Poisoned"]
food_status = ["Full","Hungry","Starving"]
drink_status = ["Full","Thirsty","Dehydrating"]
actions_options = {"wait","search"}

locations = {"forrest": "forrest_env",
                 "cabin":"cabin_env",
                 "cave": "cave_env",
                 "mountain": "mountain_env",
                 "river basin": "river_basin_env",
                 "beach": "beach_env"}

#Modules needed
import time
import random

#Current possition
c_pos = str(random.choice(list(locations.keys())))

#Start game
print ("After a long walk you got lost in a " + str(c_pos) + ".\nTry to survive and find your way back")

#Setting the location environment (in development)
#print (str(locations_dic[c_pos]))

#time.sleep(5)

#Number of turns
turns=1000
ap = 1

#Option function
def wait_for_option(options, prop):
    chosen_option = ''
    while chosen_option not in options:
        chosen_option = raw_input(prop % list(options))
        if chosen_option not in options:
            print('You have chosen an invalid option')

    return chosen_option

#Turn base loop
#time.sleep (1)
while turns > 0:
    print ("NEW TURN")
    #time.sleep (1)
    choice = raw_input("You have " + str(ap) + " action points.\n"
                                               "What you want to do?(walk / actions)\n"
                                               "R:")
    #Base walking loop
    if choice == "walk":
        path = wait_for_option(directions_options,"Which direction do you want to take? \n"
                                                  "Possible directions: %s \n"
                                                  "Your direction: ")
        if path == "north":
            print ("Walking.")
            time.sleep(1)
            print ("Walking..")
            time.sleep(1)
            print ("Walking...")
            time.sleep(1)
            turns -= 1
        else:
            print ("I've wasted my time")
    elif choice == "actions":
        action = wait_for_option(actions_options,
                                 "Which action do you want to take?\n"
                                 "Possible actions: %s\n"
                                 "Your action: ")
        if action == "wait":
            ap += 1
            print ("I've waited some time and gain some energy")

    
    
    
    
    
    
    
    
    