#Pour déterminer la résistance d'un matériau sollicité dans n'importe quelle direction O (angle)
import numpy as np
from math import *
#VALEUR A CHANGER

F11  = 1.543  #Gpa
F1   = -0.697 #Gpa
F22  = 273.30  #Gpa
F2   = 23.78 #Gpa
F12  = -10.27 #Gpa
F66  = 192.9  #Gpa

O    = (np.pi)/4     #angle en radians attention

#FIN DES VALEURS A CHANGER

c   = cos(O)
s   = sin(O)

Q2  = np.array([[c**4           ,s**4           ,2*(c**2)*(s**2)          ,(c**2)*(s**2)],
                [s**4           ,c**4            ,2*(c**2)*(s**2)          ,(c**2)*(s**2)],
                [(c**2)*(s**2)  ,(c**2)*(s**2)   ,(c**4)+(s**4)            ,-(c**2)*(s**2)],
                [4*(c**2)*(s**2),4*(c**2)*(s**2)  ,-8*(c**2)*(s**2)         ,((c**2)-(s**2))**2],
                [2*(c**3)*s      ,-2*c*(s**3)    ,2*(c*(s**3)-(c**3)*s)   ,c*(s**3)-s*(c**3)],
                [2*(s**3)*c     ,-2*s*(c**3)      ,2*(s*(c**3)-(s**3)*c)  ,s*(c**3)-c*(s**3)]])

#Calcul de F barre
f  = np.array([[F11],[F22],[F12],[F66]])

F5 = np.dot(Q2,f)

Q3 =np.array([[c**2,s**2],
              [s**2,c**2],
              [2*c*s,(-2*c*s)]])
F3 =np.array([[F1],[F2]]) 
F4 =np.dot(Q3,F3)

print('Q2')
print(Q2)
print()

print('f')
print(f)
print()

print('F2')
print(F5)
print()

print('F4')
print(F4)
print()
print('F3')
print(F3)

print()
print('Résultats sans détails')
print('F11 barre = %0.2f '%F5[0])
print('F22 barre = %0.2f '%F5[1])
print('F12 barre = %0.2f '%F5[2])
print('F66 barre = %0.2f '%F5[3])
print('F16 barre = %0.2f '%F5[4])
print('F26 barre = %0.2f\n '%F5[5])
print('F1 barre  = %0.2f '%F4[0])
print('F2 barre  = %0.2f '%F4[1])
print('F6 barre  = %0.2f '%F4[2])