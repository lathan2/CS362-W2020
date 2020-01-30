# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 18:34:00 2020

@author: lilesl

Bug introduced: the get_supply() victory cards argument is set to int(nV/nV), meaning the supply will
have 1 Estate, 1 Duchy, and 1 Province.
"""

import Dominion
import testUtility

#Get player names
player_names = ["Annie","*Ben","*Carla"]

#number of curses and victory cards
nV = testUtility.get_num_victory_cards(len(player_names))

nC = testUtility.get_num_curse_cards(len(player_names))

#Define box
box = testUtility.get_boxes(nV)

supply_order = {0:['Curse','Copper'],2:['Estate','Cellar','Chapel','Moat'],
                3:['Silver','Chancellor','Village','Woodcutter','Workshop'],
                4:['Gardens','Bureaucrat','Feast','Militia','Moneylender','Remodel','Smithy','Spy','Thief','Throne Room'],
                5:['Duchy','Market','Council Room','Festival','Laboratory','Library','Mine','Witch'],
                6:['Gold','Adventurer'],8:['Province']}

#Pick 10 cards from box to be in the supply.
supply = testUtility.get_supply(box, len(player_names), nC, int(nV/nV))

#initialize the trash
trash = []

#Costruct the Player objects
players = testUtility.get_player_objs(player_names)

#Play the game
turn = 0
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")    
    for value in supply_order:
        print(value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print(player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)

#Final score
dcs = Dominion.cardsummaries(players)
vp = dcs.loc['VICTORY POINTS']
vpmax = vp.max()

winstring = testUtility.get_win_string(vp, vpmax)

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)