# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 01:00:01 2020

@author: barde
"""
import math 

#on créer les données d'apprentissage de la forme suivante:
#A=(coordonnée selon x, coordonnée selon y, classe du point)
données_apprentissage=[[0,4,1],     
                 [3,5,0],     
                 [4,2,1],
                 [-1,0,2],
                 [4,4,3],
                 [2,-2,2],
                 [1,1,2],
                 [3,1,1],
                 [3,-8,0]
                 ]
donnée_test=[3,1]

# Fonction pour calculer la distance euclidienne entre deux points
def distance_euclidienne(point1, point2):
    distance = math.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)
    return distance



# Fonction pour localiser les voisins les plus proches
def obtenir_voisins(distance, k): 
    voisins=[]
    for i in range(k):
        voisins.append(distance[i][0])
    return voisins;

def definir_classe(voisins):
    valeurs_classe=[row[-1] for row in voisins]
    classe=max(set(valeurs_classe), key=valeurs_classe.count)
    return classe
    
def kn_voisins(données_apprentissage,donnée_test,k):  #avec k le nombre de voisins
    distance= []
    for row in données_apprentissage:
        dist = distance_euclidienne(donnée_test,row)
        distance.append((row,dist))
    distance.sort(key = lambda ligne : ligne[1])
    voisins=obtenir_voisins(distance,k)
    classe=definir_classe(voisins)
    return classe


print(str(kn_voisins(données_apprentissage,donnée_test,3)))

