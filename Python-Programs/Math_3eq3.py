import numpy as np 

# TEST MATRICE 3x3

#          | A  B  C  |   |V1|   |X|
#Matrice : | D  E  F  | x |V2| = |Y|
#          | G  H  I  |   |V3|   |Z|

X = 0.5
Y = 0.5
Z = 0  #Angle/R

A = 1
B = 1
C = 3

D = 5
E = 0
F = 1

G = 1
H = 1
I = 1


x1 = (-F*H+1)/(A-B*D-C*G+B*F*G+C*D*H-A*F*H)*E*I*X+(-B+C*H)/(A-B*D-C*G+B*F*G+C*D*H-A*F*H)*E*I*Y+(-C+B*F)/(A-B*D-C*G+B*F*G+C*D*H-A*F*H)*E*I*Z/R
x2 = (-D+F*G)/(A-B*D-C*G+B*F*G+C*D*H-A*F*H)*E*I*X+(A-C*G)/(A-B*D-C*G+B*F*G+C*D*H-A*F*H)*E*I*Y+(C*D-A*F)/(A-B*D-C*G+B*F*G+C*D*H-A*F*H)*E*I*Z/R
x3 = (-G+D*H)/(A-B*D-C*G+B*F*G+C*D*H-A*F*H)*E*I*X+(B*G-A*H)/(A-B*D-C*G+B*F*G+C*D*H-A*F*H)*E*I*Y+(A-B*D)/(A-B*D-C*G+B*F*G+C*D*H-A*F*H)*E*I*Z/R

print('V1 = %0.6f mm\nV2 = %0.6f mm\nV3 = %0.6f mm\n'%(x1,x2,x3))