import numpy as np

#Exemple de type de vis HM10-20 Classe qualité 8.8

d = 6            # Diamètre nominal de la vis mm
p = 1.25            # Pas de la vis (série pas "gros") mm
f1 = 0.15          # Coeff de frottement vis/pas de vis
f2 = 0.15          # Coeff de frottement tête/pièce
f3 = 0.2           #Coeff de frottement axe/support/rondelle
alphaS = 1.5       # Coeff incertitude clé dynamométrique
rho2 = 8           # Rayon extérieur tête de vis
rho1 = 5.5         # Rayon extérieur tige

Cserr = 2000      #Couple de serrage choisi au départ

alpha = 0*30*np.pi/180  #Angle de la tension des courroies, mettre 0 si on veut tout simplement un appui sur une vis

#Matériau
Classe=10
Multiplicateur=9

#Paramétrage fini on peut lancer le programme

d2 = d - 0.6495*p  # Diamètre moyen à flanc de filets mm
d3 = d - 1.2268*p  # Diamètre du noyaux de la vis mm
ds = (d2+d3)/2     # Diamètre section résistante mm

#Calcul auto
K1 = (0.16*p + 0.583*d2*f1)
K2 = f2*(2/3)*(rho2**3-rho1**3)/(rho2**2-rho1**2)
As = np.pi*ds**2/4
print('K1  : % 0.3f mm'%K1)
print('K2  : % 0.3f mm'%K2)
print('As : %0.2f mm2'%As)
print(" ")

FPMini = (2*Cserr)/((alphaS+1)*(K1+K2))
Tc = FPMini*f3/np.cos(alpha)
print('FPMini :  %0.f N'%FPMini)
print('Tc :  %0.f N'%Tc)
print(" ")

Re = Classe*100*Multiplicateur*0.1
F0Maxi = 0.9*Re/(np.sqrt( 1/As**2 + 3*(16*K1/(np.pi*ds**3))**2 ) )
F0Mini = F0Maxi/alphaS
F0Moy = 0.5*(F0Mini+F0Maxi)
print('F0Maxi : %0.f N'%F0Maxi)
print('F0Mini : %0.f N'%F0Mini)
print('F0Moy  : %0.f N'%F0Moy)
print(" ")

CserrMaxi = F0Maxi*(K1+K2)*(alphaS+1)/(2*alphaS)
TcMax = (F0Maxi*f3)/(alphaS*np.cos(alpha))
print('Cserr choisi  : %0.2f N.m'%(Cserr*1e-3))
print('CserrMaxi :  %0.2f N.m'%(CserrMaxi*1e-3))
print('TcMax :  %0.f N'%TcMax)
