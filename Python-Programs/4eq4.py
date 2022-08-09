#Coordonnées des points intéressants
Ligne   = [4,5,6,7]
Colonne = [4,5,6,7]


#          | A  B  C  D  |   |x1|   |Q|
#Matrice : | E  F  G  H  | x |x2| = |R|
#          | I  J  K  L  |   |x3|   |S|
#          | M  N  O  P  |   |x4|   |T|

A = Mat[Ligne[0],Colonne[0]]
B = Mat[Ligne[0],Colonne[1]]
C = Mat[Ligne[0],Colonne[2]]
D = Mat[Ligne[0],Colonne[3]]

E = Mat[Ligne[1],Colonne[0]]
F = Mat[Ligne[1],Colonne[1]]
G = Mat[Ligne[1],Colonne[2]]
H = Mat[Ligne[1],Colonne[3]]

I = Mat[Ligne[2],Colonne[0]]
J = Mat[Ligne[2],Colonne[1]]
K = Mat[Ligne[2],Colonne[2]]
L = Mat[Ligne[2],Colonne[3]]

M = Mat[Ligne[3],Colonne[0]]
N = Mat[Ligne[3],Colonne[1]]
O = Mat[Ligne[3],Colonne[2]]
P = Mat[Ligne[3],Colonne[3]]


Q = 0
R = 0
S = 0
T =-1e3


x1 = (-1000*D*G*J+1000*C*H*J+1000*D*F*K-1000*B*H*K-1000*C*F*L+1000*B*G*L)/(D*G*J*M-C*H*J*M-D*F*K*M+B*H*K*M+C*F*L*M-B*G*L*M-D*G*N+C*H*N+D*K*N-A*H*K*N-C*L*N+A*G*L*N+D*F*O-B*H*O-D*J*O+A*H*J*O+B*L*O-A*F*L*O-C*F*P+B*G*P+C*J*P-A*G*J*P-B*K*P+A*F*K*P)
x2 = (1000*D*G-1000*C*H-1000*D*K+1000*A*H*K+1000*C*L-1000*A*G*L)/(D*G*J*M-C*H*J*M-D*F*K*M+B*H*K*M+C*F*L*M-B*G*L*M-D*G*N+C*H*N+D*K*N-A*H*K*N-C*L*N+A*G*L*N+D*F*O-B*H*O-D*J*O+A*H*J*O+B*L*O-A*F*L*O-C*F*P+B*G*P+C*J*P-A*G*J*P-B*K*P+A*F*K*P)
x3 = (-1000*D*F+1000*B*H+1000*D*J-1000*A*H*J-1000*B*L+1000*A*F*L)/(D*G*J*M-C*H*J*M-D*F*K*M+B*H*K*M+C*F*L*M-B*G*L*M-D*G*N+C*H*N+D*K*N-A*H*K*N-C*L*N+A*G*L*N+D*F*O-B*H*O-D*J*O+A*H*J*O+B*L*O-A*F*L*O-C*F*P+B*G*P+C*J*P-A*G*J*P-B*K*P+A*F*K*P)
x4 = (1000*C*F-1000*B*G-1000*C*J+1000*A*G*J+1000*B*K-1000*A*F*K)/(D*G*J*M-C*H*J*M-D*F*K*M+B*H*K*M+C*F*L*M-B*G*L*M-D*G*N+C*H*N+D*K*N-A*H*K*N-C*L*N+A*G*L*N+D*F*O-B*H*O-D*J*O+A*H*J*O+B*L*O-A*F*L*O-C*F*P+B*G*P+C*J*P-A*G*J*P-B*K*P+A*F*K*P)

print('U3 = %0.6f mm\nV3 = %0.6f mm\nU4 = %0.6f mm\nV4 = %0.6f mm\n'%(x1,x2,x3,x4))