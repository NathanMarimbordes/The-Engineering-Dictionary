import numpy as np

# Tableaux des modules et largeurs :
modules  = np.array([1,1.25,1.5,1.75,2,2.5,3 ])
largeurs = np.array([8,   8, 12,  18,20,25,30])

# Tableau des nombres de dents
dentures = np.arange(12,14,1)      #Intervalle de dents pignons menants
dentures2= np.arange(13,120,1)     #Intervalle de dents pignons menés

# Couple à transmettre et rapport de réduction
i = 72/100          
C1 = 37500*i          #Nmm attention
SigFlim = 360 # Contrainte limite en MPa

#Intervalle de résultats de itrouvé
imoins =  0.9*i
iplus  =  1.1*i

#On peut choisir de minimiser une des caractéristiques de notre réducteur
#Choix possibles : 'a1' 'a3' 'DentsZ2' 'DentsZ4' 
Choix = 'DentsZ2'

#Paramétrage fini on peut lancer le programme

#Initialisation valeurs
amin1 = 1e40
Z2max = 1e40

for im1,m1 in enumerate(modules):
    m1=15.87
    m2=m1
    b1=10
    b2=b1
    for Z1 in dentures:
        Sig1 = (11*C1)/(b1*m1**2*Z1/2)
        if (Sig1<=SigFlim):
          for Z2 in dentures2:
            if Z1<Z2 :
              Sig2 = (11*C1*Z2/Z1)/(b1*m1**2*Z2/2)
              if (Sig2<=SigFlim):
                a1=m1*(Z1+Z2)/2
                if (imoins)<(Z1)/(Z2)<(iplus):
                  if Choix=='a1':
                    if a1<amin1 :
                      amin1=a1
                      i1 = Z1/Z2
                      i2 = Z3/Z4
                      itotal = i1*i2
                      print(' *** Entraxe étage 1 : %6.2fmm\t Z1 : %d\t Z2 : %d\t Module : %4.2f\t Contrainte 1 : %6.2fMPa\t Contrainte 2 : %6.2fMPa\t i1 : %6.8f'%(a1,Z1,Z2,m1,Sig1,Sig2,i1))
                      print('itotal : %6.8f\t iréel : %6.8f'%(itotal,i))
                      print("  ")
                  if Choix=='DentsZ2':
                    if Z2<Z2max :
                      Z2max=Z2
                      i1 = Z1/Z2
                      i2 = Z3/Z4
                      itotal = i1*i2
                      print(' *** Entraxe étage 1 : %6.2fmm\t Z1 : %d\t Z2 : %d\t Module : %4.2f\t Contrainte 1 : %6.2fMPa\t Contrainte 2 : %6.2fMPa\t i1 : %6.8f'%(a1,Z1,Z2,m1,Sig1,Sig2,i1))
                      print('itotal : %6.8f\t iréel : %6.8f'%(itotal,i))
                      print("  ")

