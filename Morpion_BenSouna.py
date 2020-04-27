
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 10:38:00 2020

TD4 - Morpion - Nacima Ben Souna & Marie Bardet

"""
import numpy as np
from copy import deepcopy
import math 

grille_initiale = [' ',' ',' ',' ',' ',' ',' ',' ',' ']


#affiche la grille
def affiche(s):
    print ( s[0],"|", s[1],"|", s[2])
    print ("——— ——— ———")
    print ( s[3],"|", s[4],"|", s[5])
    print ("——— ——— ———")
    print ( s[6],"|", s[7],"|", s[8])
    print(" ")
    
    
#regarde les actions possibles, là où les cases sont vides
def Actions(s):
    mvmt_possible = []
    for i in range(9):
        if s[i] == " ":
            mvmt_possible.append(i)
    return mvmt_possible

#simule l'action a dans la grille s
def Result(s, a, joueur):
    memoire = deepcopy(s)
    memoire[a] = joueur
    return memoire

#regarde si le jeu est terminé
def Terminal_test(s):
    fin = False
    for i in range (0,3): #on regarde sur les colonnes puis les lignes
        if((s[i]!=' ' and s[i]==s[i+3] and s[i+3]==s[i+6]) or
           (s[3*i]!=' ' and s[3*i]==s[3*i+1] and s[3*i+1]==s[3*i+2])):
           fin = True
    if((s[0] != ' ' and s[0] == s[4] and s[4]== s[8]) or
       (s[2] != ' ' and s[2] == s[4] and s[4]== s[6])):
            fin = True
    return fin     

#renvoie "1" si l'IA gagne, "-1" si l'humain gagne,"0" si match nul
def Utility(s):
    gain=0
    for i in range (0,3): #on regarde sur les colonnes puis les lignes
        if((s[i]==s[i+3]==s[i+6]=='X') or
           (s[3*i]==s[3*i+1]==s[3*i+2]=='X')):
           gain=1
    if((s[0] == s[4] == s[8] == 'X') or
       (s[2] == s[4] ==s[6] == 'X')):
            gain=1
    for i in range (0,3): #on regarde sur les colonnes puis les lignes
        if((s[i]==s[i+3]==s[i+6]=='O') or
           (s[3*i]==s[3*i+1]==s[3*i+2]=='O')):
           gain=-1
    if((s[0] == s[4] == s[8] == 'O') or
       (s[2] == s[4] ==s[6] == 'O')):
            gain=-1
    return gain 

#On cherche la meilleure action à jouer à l'état s 
def Minimax_decision(s):
    meilleur_score=-math.inf
    for a in Actions(s):
        score= Min_value(Result(s, a, 'X'))
        meilleur_score=max(meilleur_score,score)
    return meilleur_score

#on cherche le meilleur coup pour l'IA (celui qui lui rapporte un gain maximal)
def Max_value(s):
    if Terminal_test(s):
        return Utility(s)
    v = -math.inf
    for a in Actions(s):
        v = max(v, Min_value(Result(s, a, 'X')))
    return v

#on cherche le pire coup pour l'IA(celui qui lui rapporte un gain minimal)
def Min_value(s):
    if Terminal_test(s):
        return Utility(s)
    v = math.inf
    for a in Actions(s):
        v = min(v, Max_value(Result(s, a, 'O')))
    return v

#Partie de morpion sans l'élagage Alpha-Beta
def Morpion1():
    s = grille_initiale
    
    while not Terminal_test(s):
        a_human = eval(input("\nSaisissez la coordonnée de votre coup (de 0 à 8):"))
        s[a_human]='O'
        affiche(s)
        
        if Terminal_test(s):
            if Utility(s) == 1:
                print("\nL'IA a gagné")
            if Utility(s) == 0:
                print("\nLe match est nul")
            if Utility(s) == -1:
                print("\nVous avez gagné!")
        else:
            s[Actions(s)[Minimax_decision(s)]]='X'
            affiche(s)
            if Terminal_test(s):
                if Utility(s) == 1:
                    print("\nL'IA a gagné")
                if Utility(s) == 0:
                    print("\nLe match est nul")
                if Utility(s) == -1:
                    print("\nVous avez gagné!")

def Alpha_Beta_Search(s):
    return (np.argmax([Mini_Value_AB(Result(s,a,'X'),-math.inf,math.inf) for a in Actions(s)]))

#maximisation du gain (noeud max)
def Max_Value_AB(s,alpha,beta):
    if Terminal_test(s):
        return Utility(s)
    v=-math.inf
    for a in Actions(s):
        v=max(v,Mini_Value_AB(Result(s,a,'X'),alpha,beta))
        if v>=beta:
            return v
        alpha=max(v,alpha)
    return v 

#minimisation du gain (noeud min)
def Mini_Value_AB(s,alpha,beta):
    if Terminal_test(s):
        return Utility(s)
    v=math.inf
    for a in Actions(s):
        v=min(v,Max_Value_AB(Result(s,a,'O'),alpha,beta))
        if v<=alpha:
            return v
        beta=min(beta,v)
    return v 

#Partie de morpion avec l'élagage Alpha Beta
def Morpion2():
    s = grille_initiale
    while not Terminal_test(s):
        a_human = eval(input("\nSaisissez la coordonnée de votre coup (de 0 à 8):"))
        s[a_human]='O'
        affiche(s)
        
        if Terminal_test(s):
            if Utility(s) == 1:
                print("\nL'IA a gagné")
            if Utility(s) == 0:
                print("\nLe match est nul")
            if Utility(s) == -1:
                print("\nVous avez gagné!")
        else:
            s[Actions(s)[Alpha_Beta_Search(s)]]='X'
            affiche(s)
            if Terminal_test(s):
                if Utility(s) == 1:
                    print("\nL'IA a gagné")
                if Utility(s) == 0:
                    print("\nLe match est nul")
                if Utility(s) == -1:
                    print("\nVous avez gagné!")
    
if __name__ == '__main__':
    choix=2
    while choix!=0 or choix!=1:
        choix=input("Tapez 1 si oui,tapez 0 N si non :")
        if choix == "1":
            Morpion2()
        elif choix == "0":
            Morpion1()
