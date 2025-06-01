from email.message import _ParamsType
from sqlite3 import DataError, DatabaseError
import numpy as np 
import matplotlib.pyplot as plt  # tracé de courbes
from math import*

#######  LECTURE DU FICHIER CSV   ##########

import csv

fichier_csv='Book.csv'

with open('Book.csv') as fichier_csv:
    reader = csv.reader(fichier_csv, delimiter=';')
    for ligne in reader:
        print(ligne)


def exemple( nom_fichier_csv ):
    fichier = open(fichier_csv,"r")
    cr = csv.reader( fichier,delimiter=";")
    for row in cr:
        texte = str(len(row)) + " : "
        for i in range(len(row)):
            texte = texte + "|"+ row[i]+"|"
        print( texte )
    fichier.close()

    ##
##with open('Book.csv', newline='')) as fichier_csv:
##    reader2 = csv.reader(fichier_csv, delimiter=';')
##    for ligne in reader2:
##        print(', '.join(ligne))


##### VRAI CALCUL ##### 

x=1
y=1
resultat = x*y

print('V1 = %0.6f mm\nV2 = %0.6f mm\nV3 = %0.6f mm\n'%(x,D,resultat))



plt.figure(figsize=(40,15))
x = np.linspace(0,99,100)
plt.plot(x,resultat,'rD',linestyle = 'solid', label='Rayon statique minimal pour S=1.5')
plt.xticks(np.arange(0,101,10))
plt.yticks(np.arange(0,100,10))
plt.grid()
plt.xlabel('Largeur arbre en mm',fontsize=25)
plt.ylabel('Rayon minimal arbre en mm',fontsize=25)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.title('Approximation du diamètre minimal de l arbre',fontsize=30)



###### ECRITURE DANS LE FICHIER CSV ######

Grandeur = list["a","b","c","d","e"]
Valeur = list[1,2,3,4,5]
Unité = list["m","cm","L","m","m"]

# Créer une liste pour les en-têtes
en_tete = ["Grandeur", "Valeur", "Unité"]

# Créer un nouveau fichier pour écrire dans le fichier appelé « data.csv »
with open('Book.csv', 'w') as fichier_csv:
    # Créer un objet writer (écriture) avec ce fichier
    writer = csv.writer(fichier_csv, delimiter=',')
    writer.writerow(en_tete)
    # Parcourir les titres et descriptions - zip permet d'itérer sur deux listes ou plus à la fois
    for titre, description in zip(Grandeur, Valeur, Unité):
        # Créer une nouvelle ligne avec le titre et la description à ce moment de la boucle
        ligne = [Grandeur, Valeur, Unité]
        writer.writerow(ligne)
       


