# IMPORTS
import os
import random
import time
import sys

# VARIABLES
username = ""  # sets variable username to the default
selection = ""  # sets variable selection to the default
zombieHealth = 0  # sets variable zombieHealth to the default
userHealth = 100  # sets variable userHealth to the starting health
damageList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
              20]  # makes the list damageList - this is where a random number is pulled from to make the variable damage
room = "alpha"  # sets variable room to the first room
knifeCount = 0  # sets variable knifeCount to 0 - the user doesn't have any knives at the start


# FUNCTIONS
def cls():
    os.system("cls")  # clears the screen


def zombieFight():
    global zombieHealth, damageList, userHealth, zombieName  # makes these variables global
    damage = (random.choice(damageList))  # damage is now a random number from the list damageList
    if zombieHealth <= 0:  # if the zombie's health is 0 or less, ie the zombie is dead:
        print("Congratulations! You have successfully killed %s.\n\nYOUR HEALTH: %d" % (
        zombieName, userHealth))  # shows this
    else:
        userHealth = userHealth - damage  # takes damage off userHealth
        if userHealth <= 0:  # if the user's health is 0 or less, ie the user is dead:
            if room == "alpha":  # if the room is alpha
                cls()
                print(
                    "Uh oh! Alonzo managed to kill you. You didn't even manage to get out of the first room - that is such a fail. The console will close in 5 seconds.")  # shows this
                time.sleep(1)  # waits a second before continuing the program
                cls()
                print(
                    "Uh oh! Alonzo managed to kill you. You didn't even manage to get out of the first room - that is such a fail. The console will close in 4 seconds.")  # shows this
                time.sleep(1)  # waits a second before continuing the program
                cls()
                print(
                    "Uh oh! Alonzo managed to kill you. You didn't even manage to get out of the first room - that is such a fail. The console will close in 3 seconds.")  # shows this
                time.sleep(1)  # waits a second before continuing the program
                cls()
                print(
                    "Uh oh! Alonzo managed to kill you. You didn't even manage to get out of the first room - that is such a fail. The console will close in 2 seconds.")  # shows this
                time.sleep(1)  # waits a second before continuing the program
                cls()
                print(
                    "Uh oh! Alonzo managed to kill you. You didn't even manage to get out of the first room - that is such a fail. The console will close in 1 seconds.")  # shows this
                time.sleep(1)  # waits a second before continuing the program
                cls()
                sys.exit()  # closes the program
            else:
                cls()
                print(
                    "Uh oh! %s managed to kill you. Ah well, at least you managed to make it to room %s. The console will close in 5 seconds." % (
                    zombieName, room))  # shows this
                time.sleep(1)  # waits a second before continuing the program
                cls()
                print(
                    "Uh oh! %s managed to kill you. Ah well, at least you managed to make it to room %s. The console will close in 4 seconds." % (
                    zombieName, room))  # shows this
                time.sleep(1)  # waits a second before continuing the program
                cls()
                print(
                    "Uh oh! %s managed to kill you. Ah well, at least you managed to make it to room %s. The console will close in 3 seconds." % (
                    zombieName, room))  # shows this
                time.sleep(1)  # waits a second before continuing the program
                cls()
                print(
                    "Uh oh! %s managed to kill you. Ah well, at least you managed to make it to room %s. The console will close in 2 seconds." % (
                    zombieName, room))  # shows this
                time.sleep(1)  # waits a second before continuing the program
                cls()
                print(
                    "Uh oh! %s managed to kill you. Ah well, at least you managed to make it to room %s. The console will close in 1 second." % (
                    zombieName, room))  # shows this
                time.sleep(1)  # waits a second before continuing the program
                cls()
                sys.exit()  # closes the program
        else:
            print("He attacks you and inflicts %d damage.\n\nZOMBIE HEALTH: %d\n  YOUR HEALTH: %d" % (
            damage, zombieHealth, userHealth))  # shows this


def fight():
    global zombieHealth, damageList, selection, zombieName, knifeCount
    if knifeCount == 0:  # if the user doesn't have any knives
        selection = input(
            "Do you want to Punch, Kick, or Eye-gouge? ")  # shows this and waits for user input, which it saves as selection
        while True:  # loops continuously until statement break
            selection = selection.lower()  # makes selection lower case so the program works whether the user input CAPITALS, lower case, a MiX oF BoTH
            damage = (random.choice(damageList))  # damage is now a random number from the list damageList
            if selection == "punch" or selection == "p":  # if selection is "punch" or "p"
                cls()
                print("You punch %s and inflict %d damage." % (zombieName, damage))  # shows this
                zombieHealth = zombieHealth - damage  # takes damage off zombieHealth
                break  # breaks the loop
            elif selection == "kick" or selection == "k":  # if selection is "kick" or "k"
                cls()
                print("You kick %s and inflict %d damage." % (zombieName, damage))  # shows this
                zombieHealth = zombieHealth - damage  # takes damage off zombieHealth
                break  # breaks the loop
            elif selection == "eyegouge" or selection == "eye-gouge" or selection == "e":  # if selection is "eyegouge" or "eye-gouge" or "e"
                cls()
                print("You eye-gouge %s and inflict %d damage." % (zombieName, damage))  # shows this
                zombieHealth = zombieHealth - damage  # takes damage off zombieHealth
                break  # breaks the loop
            else:
                selection = input(
                    "I'm sorry, that is not a valid option. Please try again: ")  # shows this and waits for user input, which it saves as selection
    else:
        selection = input(
            "Do you want to Punch, Kick, Eye-gouge, or Throw your knife? ")  # shows this and waits for user input, which it saves as selection
        while True:  # loops continuously until statement break
            selection = selection.lower()  # makes selection lower case so the program works whether the user input CAPITALS, lower case, a MiX oF BoTH
            damage = (random.choice(damageList))  # damage is now a random number from the list damageList
            if selection == "punch" or selection == "p":  # if selection is "punch" or "p"
                cls()
                print("You punch %s and inflict %d damage." % (zombieName, damage))  # shows this
                zombieHealth = zombieHealth - damage  # takes damage off zombieHealth
                break  # breaks the loop
            elif selection == "kick" or selection == "k":  # if selection is "kick" or "k"
                cls()
                print("You kick %s and inflict %d damage." % (zombieName, damage))  # shows this
                zombieHealth = zombieHealth - damage  # takes damage off zombieHealth
                break  # breaks the loop
            elif selection == "eyegouge" or selection == "eye-gouge" or selection == "e":  # if selection is "eyegouge" or "eye-gouge" or "e"
                cls()
                print("You eye-gouge %s and inflict %d damage." % (zombieName, damage))  # shows this
                zombieHealth = zombieHealth - damage  # takes damage off zombieHealth
                break  # breaks the loop
            elif selection == "thrown your knife" or selection == "throw the knife" or selection == "t" or selection == "throw" or selection == "knife":  # if selection is "throw your knife" or "throw the knife" or "t" or "throw" or "knife"
                cls()
                print("You throw your knife at %s and inflict 25 damage." % zombieName)  # shows this
                zombieHealth = zombieHealth - 25  # takes 25 off zombieHealth
                break  # breaks the loop
            else:
                selection = input(
                    "I'm sorry, that is not a valid option. Please try again: ")  # shows this and waits for user input, which it saves as selection
    zombieFight()


def heal():
    global damageList, userHealth
    damage = (random.choice(damageList))  # damage is now a random number from the list damageList
    cls()
    print("You heal yourself, and gain %s health." % (damage + 1))  # shows this
    userHealth = userHealth + damage + 1  # adds 1 more than damage to userHealth (1 more so that a heal and an attack from a zombie will, on average, leave the user with more health than they've lost
    zombieFight()


def versusZombie(initialPrompt, ordinal, name):
    global zombieHealth, selection, zombieName, knifeCount
    if initialPrompt == 0:  # if the parameter initialPrompt is 0
        selection = input(
            "\nDo you want to Fight or Heal? ")  # shows this and waits for user input, which it saves as selection
    else:
        selection = input(
            initialPrompt)  # shows what is in the parameter intialPrompt and waits for user input, which it saves as selection
    zombieHealth = 20 * ordinal  # sets zombieHealth to 20 times the parameter ordinal
    zombieName = name  # sets zombieName to the parameter name

    while zombieHealth > 0:  # while zombieHealth is more than 0, ie not dead
        selection = selection.lower()  # makes selection lower case so the program works whether the user input CAPITALS, lower case, a MiX oF BoTH
        if selection == "fight" or selection == "f":  # if selection is "fight" or "f"
            fight()
            if zombieHealth > 0:  # if zombieHealth is more than 0
                selection = input(
                    "\nDo you want to Fight or Heal? ")  # shows this and waits for user input, which it saves as selection
        elif selection == "heal" or selection == "h":  # if selection is "heal" or "h"
            heal()
            if zombieHealth > 0:  # if zombieHealth is more than 0, ie the zombie is alive
                selection = input(
                    "\nDo you want to Fight or Heal? ")  # shows this and waits for user input, which it saves as selection
        else:
            selection = input(
                "I'm sorry, that is not a valid option. Please try again: ")  # shows this and waits for user input, which it saves as selection

    if lastZombie == True:  # if the zombie that was just killed was the final one in the room
        print(
            "\nCongratulations! You killed all the zombies in room %s! As you move on to the next room, you see a throwing knife, so you pick it up." % room)  # shows this
        knifeCount = knifeCount + 1  # adds 1 to knifeCount


# CODE
cls()
username = input(
    "Welcome to Operation Cranberry! What is your name? ")  # shows this and waits for user input, which it saves as username
username = ' '.join(word[0].upper() + word[1:] for word in
                    username.split())  # changes the letter at the start and every letter immediately after a space in username to capital, so their name is correctly capitalised
cls()
print(
    "Hello, %s. You are in a secret laboratory, and zombies are attacking! You need to get to room epsilon and eliminate all the zombies along your way, before they kill you first! You start off with 100 health." % username)  # shows this
lastZombie = True  # set lastZombie to True
versusZombie(
    "\nYou are in room alpha. There is one zombie in your way. He is called Alonzo, and he has a health of 20. Do you want to Fight or Heal? To select an option, either type in your choice (eg heal) or the capitalised letter of your choice (eg h): ",
    1, "Alonzo")
room = "beta"  # sets room to beta
lastZombie = False  # set lastZombie to False
versusZombie(
    "\nYou are in room beta. There are two zombies in your way. The first is called Bentley, and has a health of 20. The second is called Curien, and has a health of 40. Do you want to Fight or Heal? ",
    1, "Bentley")
lastZombie = True  # set lastZombie to True
versusZombie(0, 2, "Curien")
room = "gamma"  # sets room to gamma
lastZombie = False  # set lastZombie to False
versusZombie(
    "\nYou are in room gamma. There are three zombies in your way. The first is called Devilon, and has a health of 20. The second is called Ebitan, and has a health of 40. The third is called Flint, and has a health of 60. Do you want to Fight or Heal? ",
    1, "Devilon")
versusZombie(0, 2, "Ebitan")
lastZombie = True  # set lastZombie to True
versusZombie(0, 3, "Flint")
room = "delta"  # sets room to delta
lastZombie = False  # set lastZombie to False
versusZombie(
    "\nYou are in room delta. There are four zombies in your way. The first is called George, and has a health of 20. The second is called Hellhound, and has a health of 40. The third is called Indie, and has a health of 60. The fourth is called Junior, and has a health of 80. Do you want to Fight or Heal? ",
    1, "George")
versusZombie(0, 2, "Hellhound")
versusZombie(0, 3, "Indie")
lastZombie = True  # set lastZombie to True
versusZombie(0, 4, "Junior")
room = "epsilon"  # sets room to epsilon
lastZombie = False  # set lastZombie to False
versusZombie(
    "\nCongratulations! You have made it to room epsilon - but you aren't finished yet. There are five zombies in your way. The first is called Kierano, and has a health of 20. The second is called Lorenzo, and has a health of 40. The third is called Marc, and has a health of 60. The fourth is called Norman, and has a health of 80. The fifth is called Ollie, and has a health of 100. Do you want to Fight or Heal? ",
    1, "Kierano")
versusZombie(0, 2, "Lorenzo")
versusZombie(0, 3, "Marc")
versusZombie(0, 4, "Norman")
versusZombie(0, 5, "Ollie")
print("Congratulations %s! You beat the zombies and won the game!" % username)  # shows this