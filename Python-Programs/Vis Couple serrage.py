import numpy as np
d : 
#Exemple de type de vis CHC M10-30 Classe qualité 12.9

d = 16            # Diametre nominal de la vis mm
p = 2            # Pas de la vis (série pas "gros") mm
f1 = 0.14         # Coeff de frottement vis/pas de vis
f2 = 0.14          # Coeff de frottement tête/pièce
alphaS = 1.5       # Coeff incertitude clé dynamométrique
rho2 = 23.17/2           # Rayon extérieur tête de vis
rho1 = 17.7/2        # Rayon extérieur tige

#Matériau
Classe=8
Multiplicateur=8

#Paramétrage fini on peut lancer le programme

d2 = d - 0.6495*p  # Diamètre moyen à flanc de filets mm
d3 = d - 1.2268*p  # Diamètre du noyaux de la vis mm
ds = (d2+d3)/2     # Diamètre section résistante mm

#Calcul auto
K1 = (0.16*p + 0.583*d2*f1)
K2 = f2*(2/3)*(rho2**3-rho1**3)/(rho2**2-rho1**2)
#K2 = f2*(rho2+rho1)/2
As = np.pi*ds**2/4
print('K1  : % 0.3f mm'%K1)
print('K2  : % 0.3f mm'%K2)
print('As : %0.2f mm2'%As)
print("  ")

Re = Classe*100*Multiplicateur*0.1
F0Maxi = 0.9*Re/(np.sqrt( 1/As**2 + 3*(16*K1/(np.pi*ds**3))**2 ) )
F0Mini = F0Maxi/alphaS
F0Moy = 0.5*(F0Mini+F0Maxi)
print('F0Mini : %0.f N'%F0Mini)
print('F0Moy  : %0.f N'%F0Moy)
print('F0Maxi : %0.f N'%F0Maxi)
print(" ")

Cserr = F0Moy*(K1+K2)
Cserrmax = F0Maxi*(K1+K2)
print('Cserr  : %0.2f N.m'%(Cserr*1e-3))
print('')
print('Cserr Max  : %0.2f N.m'%(Cserrmax*1e-3))

