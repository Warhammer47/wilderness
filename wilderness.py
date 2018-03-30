# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 15:46:16 2018

@author: Pedro
"""
#Lists of objects
directions_options = {"north", "south", "east", "west"}
good_animals = ["rabbit", "bird", "bug"]
bad_animals = ["wolf", "poisonous snake"]
health_status = ["Healthy", "Injured", "Poisoned"]
food_status = ["Full", "Hungry", "Starving"]
drink_status = ["Full", "Thirsty", "Dehydrating"]
actions_options = {"wait", "search", "eat", "drink", "walk", "inventory"}

inventory = ["watch", "wallet", "LG 430", "keys"]

items = {"stone": 0.3,
         "branch": 0.2,
         "flint": 0.2,
         "berries": 0.2,
         "water bottle": 0.1}

food = {"beans": "300",
        "energy bar": "155",
        "small meat": "173"}

locations = {"forrest": "forrest_env",
             "cabin":"cabin_env",
             "cave": "cave_env",
             "mountain": "mountain_env",
             "river basin": "river_basin_env",
             "beach": "beach_env"}

#Modules needed
import time
import random
import numpy as np


#Current possition
c_pos = str(random.choice(list(locations.keys())))

#Start game
print ("After a long walk you got lost in a " + str(c_pos) + ".\nTry to survive and find your way back")

#Setting the location environment (in development)
#print (str(locations_dic[c_pos]))

#time.sleep(5)


#Option function
def wait_for_option(options, prop):
    chosen_option = ''
    while chosen_option not in options:
        chosen_option = raw_input(prop % list(options))
        if chosen_option not in options:
            print('You have chosen an invalid option')

    return chosen_option

#Number of turns
turns=1000
ap = 0

#Turn base loop
#time.sleep (1)
while turns > 0:
    print ("NEW TURN")
    ap += 5
    #time.sleep (1)
    choice = raw_input("You have " + str(ap) + " action points.\n"
                                               "What you want to do?(actions/skip)\n"
                                               "R:")
    #Base pass turn loop
    if choice == "skip":
        print("You have skip the turn")

    while ap > 0:
        # Base walking loop
        if choice == "actions":
            action = wait_for_option(actions_options,
                                     "You have " + str(ap) + " APs\n"
                                     "Which action do you want to take?\n"
                                     "Possible actions: %s\n"
                                     "Your action: ")
            if action == "inventory":
                print ("My inventory has: " + str(inventory))
            if action == "walk":
                path = wait_for_option(directions_options, "Which direction do you want to take? \n"
                                                           "Possible directions: %s \n"
                                                           "Your direction: ")
                if path == "north":
                    print ("Walking.")
                    time.sleep(1)
                    print ("Walking..")
                    time.sleep(1)
                    print ("Walking...")
                    time.sleep(1)
                    ap -= 1
            if action == "wait":
                print ("I've waited some time and gain some energy")
                ap += 1
            if action == "search":
                # Search action is defined
                print ("Searching.")
                time.sleep(1)
                print ("Searching..")
                time.sleep(1)
                print ("Searching...")
                time.sleep(1)
                ap -= 1
                new_item = np.random.choice(list(items.keys()), p=list(items.values()))
                print ("You have found: " + str(new_item))
                inventory.insert(0, str(new_item))