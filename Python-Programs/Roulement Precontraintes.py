import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
from scipy import optimize
%config InlineBackend.figure_format = 'svg'

#On initialise les valeurs des forces pr�sentes attention l'axe de rotation est Y
#Charge axiale qui ne peut �tre r�partie
Y0=0

#Forces sur les roulements 1 et 2
#Rlt1 (Rotation/Y)
X1 = 1000
Z1 = 500
Fr1 = np.sqrt(X1**2+Z1**2)
#Rlt2 (Rotation/Y)
X2 = -X1
Z2 = 758
Fr2 = np.sqrt(X2**2+Z2**2)

L1=100  #Distance entre les deux roulements

#Caract�ristiques de fonctionnement
Vitesse = 1000  #Tours/minutes
Temps = 10000   #Heures
Fiabilit� = 0.98   #Fiabilit� de montage
Fiabilit�_standard = 0.9 

# it = 0 si billes // 1 si rouleaux
it=1

# Liste des roulements test�s : (on peut en rajouter autant qu'on veut)
#          'ref'       :(d  D  Cr    e    Y_2  C)
CatRoul = {'4T-32007X' :(35,62,41500,0.45,1.32,14),
           '4T-33007'  :(35,62,50500,0.31,1.97,17),
           '4T-30207'  :(35,72,55500,0.37,1.60,15),
           '4T-32207'  :(35,72,72500,0.37,1.60,19),
           '4T-32207C' :(35,72,68000,0.58,1.03,19),
           '4T-32207CR':(35,72,62000,0.55,1.10,18),
           '4T-32008X' :(40,68,50000,0.38,1.58,14.5),
           '4T-33008'  :(40,68,59500,0.36,1.69,18)}

#choix du roulement sur lequel on va travailler
Choix = CatRoul['4T-32207']

#Type � remplacer par Hertz ou Timken
Type = 'Hertz'

#Param�trage fini on peut lancer le programme

print('Roult. R1 :\n\tX1  = %+.2f N\n\tZ1  = %+.2f N\n\tFr1 = %+.2f N'%(X1,Z1,Fr1))
print('Roult. R2 :\n\tX2  = %+.2f N\n\tZ2  = %+.2f N\n\tFr2 = %+.2f N'%(X2,Z2,Fr2))
print(" ")


L= (Temps*60*Vitesse)/1e6
print('Dur�e L : %.2f millions de tours.'%L)
print(" ")

froul = np.sqrt(Fiabilit�)
print('froul :%.3f'%froul)
print(" ")

a1 = (np.log(froul)/np.log(Fiabilit�_standard))**(2/3)
print('a1 :%.3f'%a1)
L10 = L/a1
print('L10 : %.2f millions de tours.'%L10)
print(" ")

print('Ordre de grandeur de la capacit� dynamique %.f N:'%(L10**(3/10)*max(Fr2,Fr1)))
print(" ")

## Fonction pour calculer la charge radiale �quivalente :
def Peq(Fa,Fr,e,Y2):
    if (Fa/Fr)<=e:
        Peq = Fr
    else:
        Peq = 0.4*Fr + Y2*Fa
    return Peq

# Calcul des dur�es et des charges axiales n�cessaires pour chaque
# roulement :
for ref in CatRoul:
    
    [d,D,Cr,e,Y2,c] = CatRoul[ref]
    
    # Roulement 1 -> le moins charg� axialement :
    Fa1 = 0.5*Fr1/Y2          # Charge axiale minimale pour 50% des �l�ments roulants charg�s.
    Peq1 = Peq(Fa1,Fr1,e,Y2)  # Charge radiale �quivalente correspondante.
    L101 = (Cr/Peq1)**(10/3)  # Dur�e de vie en millions de tours.
    
    # Roulement 2 -> le plus charg� axialement :
    Fa2min = 0.5*Fr2/Y2       # Charge axiale minimale pour 50% des �l�ments roulants charg�s.
    Fa2 = Fa1 + np.abs(Y0)    # Charge axiale tir�e  du PFD
    Peq2 = Peq(Fa2,Fr2,e,Y2)  # Charge radiale �quivalente correspondante.
    L102 = (Cr/Peq2)**(10/3)  # Dur�e de vie en millions de tours.

    print(ref)
    print('R1 : Fa1 (50%%)        : %.2f N\t\tFr1 : %.2f N\tPeq1 : %.2f N   L10_1 : %.2f'%(Fa1,Fr1,Peq1,L101))
    print('R2 : Fa2 (PFD)/(50%%)  : %.2f/%.2f N\tFr2 : %.2f N\tPeq2 : %.2f N   L10_2 : %.2f'%(Fa2,Fa2min,Fr2,Peq2,L102))
    print(('-')*100)
    print(" ")

## Calcul et Ttrac� de la fonction f(a,t) :
# Borne d'int�gration :
def Borne(a):
    return  np.arccos(-min(a,1.0))

def Xi(a,t):
    dXi  = lambda x:(np.cos(x)+a)**(1/t)
    # Xi calcul�e par int�gration num�rique:
    Xi = 1/(2*np.pi)*integrate.quad(dXi,-Borne(a),Borne(a))[0]
    return Xi

def Psi(a,t):
    dPsi  =  lambda x:np.cos(x)*(np.cos(x)+a)**(1/t)
    # Phi calcul�e par int�gration num�rique:
    borne = Borne(a)
    Psi = 1/(2*np.pi)*integrate.quad(dPsi,-Borne(a),Borne(a))[0]
    return Psi


T=((2/3,'2/3'),(0.9,'0.9'))
t= T[it][0]
tt = T[it][1]
ValXi = []
ValPsi = []
# Pour les valeurs de a entre -1 et 3
A = np.linspace(-1,2,200)
for a in A: 
    ValXi.append(Xi(a,t))
    ValPsi.append(Psi(a,t))          

# Trac� des courbes :
ValXi = np.array(ValXi)
ValPsi = np.array(ValPsi)
# Pour �viter le pb de la division par 0 pour a=-1.
f = np.full_like(ValPsi,1)
f[1:] = ValXi[1:]/ValPsi[1:]
plt.figure(figsize=(8,8))
plt.plot(A,ValXi,'r-',label=r'$\xi(a,$'+tt+'$)$')
plt.plot(A,ValPsi,'b-',label=r'$\psi(a,$'+tt+'$)$')
plt.plot(A,f,'g-',linewidth=3,label=r'$f(a,$'+tt+'$)$')
plt.xlim(-1,1)
plt.ylim(0,3)
plt.xlabel('Param�tre de charge $a$')
plt.xticks(np.arange(-1,2,0.2))
plt.yticks(np.arange(0,3,0.2))
plt.grid()
plt.legend(fontsize=12)



Xi(0,0.9)/Psi(0,0.9)
# Recup�re les caract�ristiques du roulement :
[d,D,Cr,e,Y2,C] = Choix
# Recalcule les valeurs des efforts axiaux pour ce roulement
Fa1 = 0.5*Fr1/Y2  
Fa2 = Fa1 + np.abs(Y0)  
f_a1 = Xi(0,0.9)/Psi(0,0.9)
alpha =np.arctan(0.5/(Y2*f_a1))
print('alpha : %.2f deg'%(alpha*180/np.pi))
print(" ")

f_a2 = Fa2/(np.tan(alpha)*Fr2)
print('f_a2 : %.4f'%f_a2)
print(" ")

# R�solution num�rique avec une m�thode de la s�cante :
# On d�finit la fonction � r�soudre -> =0
fzero = lambda x:(Xi(x,0.9)/Psi(x,0.9)-f_a2)

sol = optimize.root_scalar(fzero, x0=1.4,x1=1.6, method='secant')
a2=sol.root
print('a2 : %.5f'%a2)
print(" ")

# Raideur locale des rouleaux :
def Kloc(L,D):
    if Type=='Hertz':
      Kloc = (2*3.78e-05)/(L**0.8)          # Raideur rouleaux cylindrique "Hertz"
    if Type=='Timken':
      Kloc = (1.45e-04)/(L**0.9*D**0.094)   # Raideur rouleaux coniques "Timken"
    return Kloc

# Nombre de rouleaux :
Dw = 0.317*(D-d)
Dm = (D+d)/2
Z = int(np.pi*Dm/Dw)-2
Z = 14 # Info tir�e de la CAO du catalogue constructeur
L = C/np.cos(alpha)
Kr = Z*np.cos(alpha)*(np.cos(alpha)/Kloc(L,D))**(1/0.9)

# Raideur SKF :
#Kskf = 2.14e-5/(L**0.5)
#Kr = Z*np.cos(alpha)*(np.cos(alpha)/Kskf)**(1/0.9)

# D�placement de R1 :
dr1 = (Fr1/(Kr*Psi(0,0.9)))**0.9
da1 = 0

# D�placement de R2 :
dr2 = (Fr2/(Kr*Psi(a2,0.9)))**0.9
da2 = a2*dr2/(np.tan(alpha))
print ('Pour R1 et R2 :\n\tZ : %2i rouleaux'%Z)
print ('\tRaideur locale 1/(Ki+Ke) :%.3e N^(0.9).mm^(-1.8)'%(1/Kloc(L,D)))
print ('\tRaideur globale Kr       :%.3e N.mm^(-1/0.9)'%Kr)
print ('Pour R1:\n\tda1 : %.5f mm\n\tdr1 : %.5f mm'%(da1,dr1))
print ('Pour R2:\n\tda2 : %.5f mm\n\tdr2 : %.5f mm'%(da2,dr2))
print(" ")

datotal=da1+da2
print ('Pr�contrainte au montage impos�e de  :%.3e mm'%datotal)


