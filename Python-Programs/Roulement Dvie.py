import numpy as np

# Données roulements à absolument vérifier
# Le modèle ici est le : 30161006
d = 30
D = 60
B = 20
C = 20700
C0 = 11300
e = 0.17
X1 = 1
X2 = 0.6
Y1 = 0
Y2 = 0.5

f0=1.5

# Données chargement en fonction des phases :
Fx = [100,100,100]                            #[Force]
Fy = [50,50,50]                            #[Force]
Phase =[[100,100],[75,100],[100,100]]   #[vitesse rot,temps utilisation]
L = 0.5

# Fonction de calcul de la charge radiale équivalente
def Peq(Fa,Fr,e,X1,X2,Y1,Y2):
    if ((Fa/Fr)<=e):
        P = X1*Fr + Y1*Fa
    else:
        P = X2*Fr + Y2*Fa
    return P

def P0(Fa,Fr):
  P20=1.5*(0.6*Fr+0.6*Fa)
  return P20

LP = []
# Pour toutes les phases de chargement ...
for i,(fx,fy) in enumerate(zip(Fx,Fy)):
    Fr = np.abs(-(1+L)*fy)
    Fa = np.abs(-fx)
    P = Peq(Fa,Fr,e,X1,X2,Y1,Y2)
    print('Phase %i | Fr  %8.2f | Fa  %8.2f | Peq  %8.2f N'%(i,Fr,Fa,P))
    P20=P0(Fa,Fr)
    print('Charge équivalente statique P0 = %8.2f N'%P20)
    e=0.51*(Fa/C0)**0.23
    Y=0.87*(Fa/C0)**(-0.23)
    X=0.56
    print('e = %8.2f\t X = %8.2f\t Y = %8.2f\t'%(e,X,Y))
    print("  ")

    LP.append(P)
    
# Initialise les variables pour les sommes ..
Utot = 0   # Somme des Ui
UPtot = 0 # Somme des Ui.Pi pour le rlt
# Calcul des sommes pour les 3 phases ..
for phasei,Pi in zip(Phase,LP):
    Ui = phasei[0]*phasei[1]
    Utot = Utot + Ui
    UPtot = UPtot  + Ui*(Pi**3)

Peq = (UPtot/Utot)**(1/3)
print('Charge radiale équiv.\n\tRlt.  %8.2f N'%(Peq))
print("  ")

L10 = (C/Peq)**3
print('Durée de vie à 90%% en million de tours:\n\t*Rlt.  %.0f'%(L10))
print("  ")

sumL10 = L10**(-3/2)
L = ( np.log(0.95)/(np.log(0.9)*sumL10) )**(2/3)
print('Durée de vie :\n\t*En millions de tours : %.f'%L)
print("  ")

# Utot est le nbre de tour en une minute pour les 3 phases -> somme des Ui
Lh = L*1e6/(Utot*60)
print('Durée de vie :\n\t*En heures : %.2f \n'%Lh)

print('Durée de vie totale de tous les paliers en série\n')
LE10=(6*(1/L10)**1.5)**(-1/1.5)
LEh=( np.log(0.95)/(np.log(0.9)*LE10**(-3/2)) )**(2/3)*1e6/(Utot*60)
print('Durée de vie à 90%% en million de tours:\n\t*Rlt.  %.0f'%(LE10))
print('Durée de vie :\n\t*En heures : %.2f \n'%LEh)