# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 16:13:06 2024

@author: USER
"""

# =====================================
#             Saisie interactive
#======================================
#%%
# demander au user de saisir son nom
nom = input("Quel est votre nom ?")
# afficher le nom
print("Il s'appelle ", nom)

# demander la taille du user
taille = input("Quelle est votre taille ?")
# affichier la taille
print("Il mesure", taille, "m")

# coercition
taille = float(taille)

# saisie interactive et coercition
x = int(input("saisir la 1re valeur numérique :"))
y = int(input("saisir une 2nde valeur numérique :"))
# afficher la somme
print("res = ", x + y )

# saisir des tableaux
lettres = list(input("Entrer des lettres : "))
print(lettres)
lettre_2 = tuple(input("Entrer d'autres lettres : "))
print(lettre_2)