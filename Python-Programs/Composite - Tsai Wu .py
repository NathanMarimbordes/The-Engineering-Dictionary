#VALEUR A CHANGER

F11  = 1.543  #Gpa
F1   = -0.697 #Gpa
F22  = 273.30  #Gpa
F2   = 23.78 #Gpa
F12  = -10.27 #Gpa
F66  = 192.9  #Gpa

σ1   = 50    #Mpa 
σ2   = 20    #Mpa
σ6   = 22      #Mpa

#FIN DES VALEURS A CHANGER

C    = F11*((σ1*(10**-3))**2)+2*F12*(σ1*(10**-3))*(σ2*(10**-3))+F22*((σ2*(10**-3))**2)+F66*((σ6*(10**-3))**2)+F1*(σ1*(10**-3))+F2*(σ2*(10**-3))

print(C)

#Calcul de R = coefficient de sécurité
import numpy as np


b  = F1*(σ1*(10**-3))+F2*(σ2*(10**-3))
c  = -1
a  = F11*((σ1*(10**-3))**2)+2*F12*(σ1*(10**-3))*(σ2*(10**-3))+F22*((σ2*(10**-3))**2)+F66*((σ6*(10**-3))**2)

D  = (b**2)-4*a*c

print('Valeur de Delta = %0.5f'%(D))
print('Valeur de a = %0.5f'%(a))
print('Valeur de b = %0.5f'%(b))
print('Valeur de c = %0.5f'%(c))
print()


#executer ssi D=0 CALCUL DE SOLUTION UNIQUE
R  = -b/(2*a)
print(R)

#Si un des R est négatif c'est pour les même valeurs absolue de contrainte mais de sens opposé.

#executer ssi D>0
R1 = (-b-np.sqrt(D))/(2*a)
R2 = (-b+(np.sqrt(D)))/(2*a)

print(R1,R2)