# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 16:38:09 2021

@author: Oktan Burg
Github: https://github.com/Oktan-Burg/Python-basics
Youtube: https://www.youtube.com/channel/UCSU4rYDGsp8PGhrgWMRx2cg
"""
#Create variables
gamers = [('oktan burg',20),('ninja',42),('deathstar234',40)]
#Create fuction
def wincheck(gamers):
    maxkills = 0
    winner = ''
    for plr,kills in gamers:
        if kills > maxkills:
            maxkills = kills
            winner = plr
        else:
            pass
     print('The winner is ' + winner + ' with ' + str(maxkills) + ' kills.')
