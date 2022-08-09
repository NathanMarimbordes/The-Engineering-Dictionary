import numpy as np
from math import *

E1  = 40
E2  = 10
v12 = 0.32
G12 = 4.56
 
t   = np.pi/6   #Angle téta en RADIAN

σx  = 0.01
σy  = -0.005
τxy = 0.02


#Fin valeur à remplir

c = cos(t)
s = sin(t)

S11 = E1/(1-(E2/E1)*v12**2)
S22 = S11*(E2/E1)
S12 = v12*S22
S66 = G12




P  = np.array([[c**4,s**4,2*(c**2)*(s**2),(c**2)*(s**2)],
[s**4,c**4,2*(c**2)*(s**2),(c**2)*(s**2)],
[(c**2)*(s**2),(c**2)*(s**2),(c**4)+(s**4),-1*(c**2)*(s**2)],
[4*(c**2)*(s**2),4*(c**2)*(s**2),-8*(c**2)*(s**2),((c**2)-(s**2))**2],
[2*(c**3)*s,-2*c*(s**3),2*((c*(s**3)-(c**3)*s)),(c*(s**3)-s*(c**3))],
[2*(s**3)*c,-2*s*(c**3),2*(s*(c**3)-(s**3)*c),(s*(c**3)-c*(s**3))]])

q  = np.array([[S11],[S22],[S12],[S66]])

F = np.dot(P,q)

print('S11 barre = %0.18f '%F[0])
print('S22 barre = %0.18f '%F[1])
print('S12 barre = %0.18f '%F[2])
print('S66 barre = %0.18f '%F[3])
print('S16 barre = %0.18f '%F[4])
print('S26 barre = %0.18f \n'%F[5])

S111 = float(F[0])
S222 = float(F[1])
S121 = float(F[2])
S666 = float(F[3])
S161 = float(F[4])
S261 = float(F[5])

P1 = np.array([[S111,S121,S161],
               [S121,S222,S261],
               [S161,S261,S666]])

ep  = np.array([[σx],
                [σy],
                [τxy]])

print(P1.shape)
print(ep.shape)

S = np.dot(P1,ep)

print('\nP1')
print(P1)
print('\n ep')
print(ep)
print('\n S')
print( S)

print('\nεx  = %0.18f '%S[0])
print('εy  = %0.18f '%S[1])
print('γxy = %0.18f '%S[2])

εx = float(S[0])
εy = float(S[1])
γxy = float(S[2])

P2 = np.array([[c**2,s**2,c*s],
              [s**2,c**2,-1*c*s],
              [-2*c*s,2*c*s,c**2-s**2]])

q2 =np.array([[εx],[εy],[γxy]])

F2 = np.dot(P2,q2)

print('\nε1  = %0.18f '%F2[0])
print('ε2  = %0.18f '%F2[1])
print('γ12 = %0.18f '%F2[2])