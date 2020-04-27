#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 22:39:28 2020

@author: nacimabensouna
"""

from ortools.sat.python import cp_model
import numpy

 #create the model
model = cp_model.CpModel()
    
#creates variables
kbase = 9

l=[]

for i in range(1,10):
    l.append([model.NewIntVar(1,9,"case"+str(i)+str(j)) for j in range(1,10)])
print(l)

print("\n---------------------------------\n")
    


print("\n-------------SUDOKU---------------\n")

grille={}

for i in range(0,9):
    for j in range(0,9):
        grille[i,j]=(model.NewIntVar(1,kbase,'var'))

#create the contraints
        
#Contrainte sur les lignes : un nombre ne peut pas apparaitre plus d'une fois sur la même ligne.
#On applique AllDifferent sur les lignes. 
        
for i in range(0,9):
    model.AddAllDifferent([grille[(i, j)]for j in range(0,9)])
        
#Contrainte sur les colonnes : un nombre ne peut pas apparaitre plus d'une fois dans la même colonne
#On applique AllDifferent sur les colonnes.
        
for j in range(0,9):
    model.AddAllDifferent([grille[(i, j)] for i in range(0,9)])

#Contrainte sur les cases : Au sein d'une case un nombre ne peut pas apparaitre plus d'une fois .
#On applique AllDifferent sur chaque case

for i in range(0,3):
    for j in range(0,3):
        case = [grille[(3*i + a,3*j+ b)] for a in range(0,3)    for b in range(0,3)] 
        model.AddAllDifferent(case)
             

#Remplissage de la grille 
           
for i in range(0,9):
    for j in range(0,9):
        model.Add(grille[(i, j)] == l[i][j])

#create a solver and solve the model
solver = cp_model.CpSolver()
status = solver.Solve(model)

l2=[]  
  
if status == cp_model.FEASIBLE: 
    for i in range(0,9):
        sudoku=[int(solver.Value(grille[(i, j)])) for j in range(0,9)]
        print(sudoku)
        l2.append(sudoku)
        
print("\n................\n")

#Affichage grille selon niveau de difficulté
print("\nChoisir un niveau de difficulté")
print("\n................\n")
print("1 : Très difficile.\n2 : Difficile.\n3 : Moyen.\n4 : Facile.\n5 : Débutant.")
print("\n................\n")
x=input()

if(x=="1"):#Affiche seulement 17 valeurs
    for i in range(0,9):
        for j in range(0,9):
            if (i!=j and j!=(8-i)):
                l2[i][j]=0

if(x=="2"):#Affiche seulement 26 valeurs
    for i in range(0,9):
        for j in range(0,9):
            if(j!=4):
                if (j%2!=0 or j%3==0):
                    l2[i][j]=0
            else:
                if(j==i==4):
                    l2[i][j]=0
        
if(x=="3"):#Affiche seulement 33 valeurs
    for i in range(0,9):
        for j in range(0,9):
            if (i%2==0):
                if (j%3==0 and j==6):
                    l2[i][j]=0
                
            if (i%3==0):
                if (j%3==0):
                    l2[i][j]=0
            else:
                if (j%3!=0):
                    l2[i][j]=0  
        
if(x=="4"):#Affiche seulement 40 valeurs
    for i in range(0,9):
        for j in range(0,9):
            if (i%2==0):
                if (j%2==0):
                    l2[i][j]=0
            else:
                if (j%2!=0):
                    l2[i][j]=0
        
if(x=="5"):#Affiche seulement 50 valeurs
    for i in range(0,9):
        for j in range(0,9):
            if (i%2==0):
                if (j%2!=0 and j!=1):
                    l2[i][j]=0
            else:
                if (j%2==0 and j!=8):
                    l2[i][j]=0


 # Affichage grille de sudoku
print("\n................\n") 
print("\nGrille de sudoku niveau "+x+" :\n")   
sudoku=numpy.zeros(shape=(9,9))
for i in range(0,9):
    for j in range(0,9):
        sudoku[i,j]=l2[i][j]
       
print(sudoku)