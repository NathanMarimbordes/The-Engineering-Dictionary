import numpy as np
from math import *

E1  = 40     #Si en GPa alors résultat en Gpa
E2  = 10
v12 = 0.32
G12 = 4.56
 
t   = np.pi/6   #Angle téta en RADIAN

εx  = 0.01
εy  = -0.005
γxy = 0.02

#Fin valeur à remplir

c = cos(t)
s = sin(t)

Q11 = E1/(1-(E2/E1)*v12**2)
Q22 = Q11*(E2/E1)
Q12 = v12*Q22
Q66 = G12




P  = np.array([[c**4,s**4,2*(c**2)*(s**2),4*(c**2)*(s**2)],
[s**4,c**4,2*(c**2)*(s**2),4*(c**2)*(s**2)],
[(c**2)*(s**2),(c**2)*(s**2),(c**4)+(s**4),-4*(c**2)*(s**2)],
[(c**2)*(s**2),(c**2)*(s**2),-2*(c**2)*(s**2),((c**2)-(s**2))**2],
[(c**3)*s,-1*c*(s**3),(c*(s**3)-(c**3)*s),2*(c*(s**3)-s*(c**3))],
[(s**3)*c,-1*s*(c**3),s*(c**3)-(s**3)*c,2*(s*(c**3)-c*(s**3))]])

q  = np.array([[Q11],[Q22],[Q12],[Q66]])

F = np.dot(P,q)

print('Q11 barre = %0.18f '%F[0])
print('Q22 barre = %0.18f '%F[1])
print('Q12 barre = %0.18f '%F[2])
print('Q66 barre = %0.18f '%F[3])
print('Q16 barre = %0.18f '%F[4])
print('Q26 barre = %0.18f \n'%F[5])

Q111 = float(F[0])
Q222 = float(F[1])
Q121 = float(F[2])
Q666 = float(F[3])
Q161 = float(F[4])
Q261 = float(F[5])

P1 = np.array([[Q111,Q121,Q161],
               [Q121,Q222,Q261],
               [Q161,Q261,Q666]])

ep  = np.array([[εx],[εy],[γxy]])

print(P1.shape)
print(ep.shape)

S = np.dot(P1,ep)

print('\nP1')
print(P1)
print('\n ep')
print(ep)
print('\n S')
print( S)

print('\nσx  = %0.18f '%S[0])
print('σy  = %0.18f '%S[1])
print('τxy = %0.18f '%S[2])

σx = float(S[0])
σy = float(S[1])
τxy = float(S[2])

P2 = np.array([[c**2,s**2,2*c*s],
              [s**2,c**2,-2*c*s],
              [-1*c*s,c*s,c**2-s**2]])

q2 =np.array([[σx],[σy],[τxy]])

print('\nP2')
print(P2)

F2 = np.dot(P2,q2)

print('\nσ1  = %0.18f '%F2[0])
print('σ2  = %0.18f '%F2[1])
print('τ12 = %0.18f '%F2[2])
