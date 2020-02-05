# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 18:34:00 2020

@author: lilesl
"""

import Dominion
import random
from collections import defaultdict


def get_boxes(nV):
    """
    :param nV: starting number of each victory card, used here
    for calculating number of garden cards
    :return: box, a dictionary containing starting lists of action cards
    """
    box = {}
    box["Woodcutter"] = [Dominion.Woodcutter()] * 10
    box["Smithy"] = [Dominion.Smithy()] * 10
    box["Laboratory"] = [Dominion.Laboratory()] * 10
    box["Village"] = [Dominion.Village()] * 10
    box["Festival"] = [Dominion.Festival()] * 10
    box["Market"] = [Dominion.Market()] * 10
    box["Chancellor"] = [Dominion.Chancellor()] * 10
    box["Workshop"] = [Dominion.Workshop()] * 10
    box["Moneylender"] = [Dominion.Moneylender()] * 10
    box["Chapel"] = [Dominion.Chapel()] * 10
    box["Cellar"] = [Dominion.Cellar()] * 10
    box["Remodel"] = [Dominion.Remodel()] * 10
    box["Adventurer"] = [Dominion.Adventurer()] * 10
    box["Feast"] = [Dominion.Feast()] * 10
    box["Mine"] = [Dominion.Mine()] * 10
    box["Library"] = [Dominion.Library()] * 10
    box["Gardens"] = [Dominion.Gardens()] * nV
    box["Moat"] = [Dominion.Moat()] * 10
    box["Council Room"] = [Dominion.Council_Room()] * 10
    box["Witch"] = [Dominion.Witch()] * 10
    box["Bureaucrat"] = [Dominion.Bureaucrat()] * 10
    box["Militia"] = [Dominion.Militia()] * 10
    box["Spy"] = [Dominion.Spy()] * 10
    box["Thief"] = [Dominion.Thief()] * 10
    box["Throne Room"] = [Dominion.Throne_Room()] * 10

    return box


def get_num_victory_cards(num_players):
    """
    :param num_players: number of players
    :return: starting number of each victory card
    """
    if num_players > 2:
        return 12
    else:
        return 8


def get_num_curse_cards(num_players):
    """
    :param num_players: number of players
    :return: starting number of curse cards
    """
    return -10 + 10 * num_players


def get_supply(box, num_players, nC, nV):
    """
    :param box: dictionary containing starting lists of action cards
    :param num_players: number of players
    :param nC: starting number of curse cards
    :param nV: starting number of each victory card
    :return: dictionary of 10 randomly selected action cards and a
    prescribed amount of coin, victory, and curse cards (according
    to this function)
    """
    boxlist = [k for k in box]
    random.shuffle(boxlist)
    random10 = boxlist[:10]
    supply = defaultdict(list, [(k, box[k]) for k in random10])

    # The supply always has these cards
    supply["Copper"] = [Dominion.Copper()] * (60 - num_players * 7)
    supply["Silver"] = [Dominion.Silver()] * 40
    supply["Gold"] = [Dominion.Gold()] * 30
    supply["Estate"] = [Dominion.Estate()] * nV
    supply["Duchy"] = [Dominion.Duchy()] * nV
    supply["Province"] = [Dominion.Province()] * nV
    supply["Curse"] = [Dominion.Curse()] * nC

    return supply


def get_player_objs(player_names):
    """
    :param player_names: names of the players
    :return: list of player objects
    """
    players = []
    for name in player_names:
        if name[0] == "*":
            players.append(Dominion.ComputerPlayer(name[1:]))
        elif name[0] == "^":
            players.append(Dominion.TablePlayer(name[1:]))
        else:
            players.append(Dominion.Player(name))

    return players


def get_win_string(vp, vpmax):
    """
    :param vp: pandas dataframe which contains the number of victory points each player has
    :param vpmax: the number of victory points the player with the most victory points has
    :return: string announcing all victors
    """
    winners = []
    for i in vp.index:
        if vp.loc[i] == vpmax:
            winners.append(i)
    if len(winners) > 1:
        winstring = ' and '.join(winners) + ' win!'
    else:
        winstring = ' '.join([winners[0], 'wins!'])

    return winstring

 

