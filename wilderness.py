# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 15:46:16 2018

@author: Pedro
"""

####################################################
###################### NOTES #######################
####################################################

#AP (actions points) is the expressed in minutes and is the amount you have in each turn
            #It can be used in actions


####################################################
#################### END NOTES #####################
####################################################


#Modules needed
import time
import random
import numpy as np

#Lists of objects
directions_options = {"north", "south", "east", "west"}
good_animals = ["rabbit", "bird", "bug"]
bad_animals = ["wolf", "poisonous snake"]
health_status = ["Healthy", "Injured", "Poisoned"]
food_status = ["Full", "Hungry", "Starving"]
drink_status = ["Full", "Thirsty", "Dehydrating"]

general_options = {"actions", "skip"}

actions_options = {"wait", "search", "eat", "drink", "walk", "inventory", "status", "return"}

inventory = ["watch", "wallet", "LG 430", "keys"]

items = {"stone": 0.3,
         "branch": 0.2,
         "flint": 0.2,
         "berries": 0.1,
         "Penacova 0.33cl": 0.1,
         "empty": 0.1}

food_items = {"beans": "300",
              "energy bar": "155",
              "small meat": "173"}

locations = {"forrest": "forrest_env",
             "cabin":"cabin_env",
             "cave": "cave_env",
             "mountain": "mountain_env",
             "river basin": "river_basin_env",
             "beach": "beach_env"}

# Defining status
# in ml (max = 2000)
# in calories (max = 2000)
# in hours of sleep (max = 8)
# Health (max = 100)
status = {"drink": 2000,
          "food": 2000,
          "sleep": 9,
          "health": 100}

#Current position
position = str(random.choice(list(locations.keys())))

#Start game
print ("After a long walk you got lost in a " + str(position) + ".\nTry to survive and find your way back")

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
while turns > 0:
    print ("NEW TURN")
    ap += 60

    while True:
        choice = wait_for_option(general_options, "You have " + str(ap) + " APs.\n"
                                                                          "What you want to do?(actions/skip)\n"
                                                                          "R:")
        # Death outcome
        if status["health"] <= 0:
            print("You died...")
            break

        # Pass turn
        if choice == "skip":
            print("You have skip the turn")

        # Basic actions
        while ap > 0:
            if choice == "actions":
                action = wait_for_option(actions_options,
                                         "You have " + str(ap) + " APs\n"
                                                                 "Which action do you want to take?\n"
                                                                 "Possible actions: %s\n"
                                                                 "Your action: ")
                # Return to main menu option
                if action == "return":
                    break

                # Check status
                if action == "status":
                    for key in status:
                        print key, status[key]

                # Check inventory
                if action == "inventory":
                    print ("My inventory has: " + str(inventory))

                # Base walking
                if action == "walk":
                    if ap >= 60:
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
                            ap = ap - 60

                # Base wait (it is being decided if it will be implemented or not)
                #if action == "wait":
                    #print ("I've waited some time and gain some energy")
                    #ap = ap + 10

                # Base search
                if action == "search":
                    if ap >= 30:
                        # Search action is defined
                        print ("Searching.")
                        time.sleep(1)
                        print ("Searching..")
                        time.sleep(1)
                        print ("Searching...")
                        time.sleep(1)
                        ap = ap - 30
                        new_item = np.random.choice(list(items.keys()), p=list(items.values()))
                        if new_item == "empty":
                            print "You have found nothing"
                        else:
                            print("You have found: " + str(new_item))
                            inventory.insert(0, str(new_item))
                    else:
                        print "You don't have enough AP"

        # 3 Days without water = loss of 27.8mL/hour
        status["drink"] = status["drink"] - 27.8
        # 30 Days without food = loss of 2.8cal/hour
        status["food"] = status["food"] - 2.8
        # 3 Days without sleep = loss of 0.125 hours of sleep/hour
        status["sleep"] = status["sleep"] - 0.125


print ("Game ended")
