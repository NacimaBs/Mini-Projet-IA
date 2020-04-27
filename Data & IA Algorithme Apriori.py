#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 21:05:43 2020

@author: nacimabensouna
"""
print("Algorithme Apriori :")
print("Considerons la liste d'élement suivante :")
L= [1,2,5],[1,3,5],[1,2],[1,2,3,4,5],[1,2,4,5],[2,3,5],[1,5]
occ=0
print (L)

print("Calcul du support:")

def calcul1(L,occ):
    Liste=[[],[],[],[],[],[],[]]
    for i in range (1,6):
        for j in range (0,len(L)):
            occ=L[j].count(i)
            Liste[j]=occ
        somme=0
        for k in range (0,7):
            somme=Liste[k]+somme
        somme=somme/7
        if (somme>0.3):
            print("Support de " + str(i)+ ' est '+ str(round(somme,2)))
            occ=0
            
def calcul2(L,occ):
    Liste=[[],[],[],[],[],[],[]]
    somme=0
    for m in range (1,6):
        for n in range (1,6):
            if (m != n):
                for o in range (0,len(L)):
                    occ=0
                    occ=L[o].count(m) and L[o].count(n)
                    Liste[o]=occ
               # for p in range (0,7):
                    #somme = somme  L[p]
                #somme=somme/7
                   
                if (somme>0.30):
                    print( "Support de ["+ str(m) + "," + str(n) + "] = " + str(round(somme, 2)) )
                    somme = 0
    
def calcul3(L, occ):
    
    Liste = [ [], [], [], [], [], [], [] ]
    somme = 0
    
    for i in range(1,6):
        for j in range(1,6):
            for k in range(1,6):
                if(i!=j and i!=k and j!=k):
                    for m in range(0,len(L)):
                        occ = 0
                        occ = L[m].count(i) and L[m].count(j) and L[m].count(k)
                        Liste[m] = occ  
                        
                    for n in range(0,7):
                        somme = somme + Liste[n]
                    somme = somme/7
                    if(somme > 0.30):                    
                        print("Support de ["+ str(i) + "," + str(j) + "," + str(k) + "] = " + str(round(somme, 2)) )
                    somme = 0

def calculSupport():

    calcul1(L, occ)
    calcul2(L, occ)  
    calcul3(L, occ)
    

def calculSupport1(L, occ, n):
    
    somme2=0
    Liste = [ [], [], [], [], [], [], [] ]
    for i in range(0,len(L)):
        occ = L[i].count(n)
        Liste[i] = occ
        
    for j in range(0,7):
        somme2 = Liste[j] + somme2
    somme2 = somme2/7
    return round(somme2, 2)

def calculSupport2(L, occ, n, m):
    
    somme = 0
    Liste = [ [], [], [], [], [], [], [] ]
    for i in range(0,len(L)):
        occ = L[i].count(n) and L[i].count(m)
        Liste[i] = occ   
                    
    for j in range(0,7):
        somme = somme + Liste[j]
    somme = somme/7
    return round(somme, 2)


def calculConf(L, occ): 
    
    dict1 = { }
    for i in range(1,6):
        dict1[i] = calculSupport1(L, occ, i)
    
    dict2 = { }
    for j in range(1,6):
        for k in range(1,6):
            if(j!=k):
                dict2[j,k] = calculSupport2(L, occ, j, k)
        
    for l in range(1,6):
        for m in range(1,6):
            if(l !=m):
                print("La confiance de : (" + str(l) + "," + str(m) + ") avec " + str(l) + " = " + str( round(dict2[l,m]/dict1[l],2)) )
    
if __name__ == "__main__":
    
    print("\nCalcul support > 0.30\n")
    calculSupport()
    print("\nCalcul confiance > 0.25\n")
    calculConf(L, occ)
                
     
          
           

