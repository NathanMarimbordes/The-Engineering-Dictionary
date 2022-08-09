from sympy import *                  # Libraire de calculs symboliquen docs->http://www.sympy.org
from sympy.vector import CoordSys3D  # Module de gestion des vecteurs de sympy.
from IPython.display import display, Latex
# On d�fini les variables symboliques qui seront utilis�es
# dans les calculs.
a,b,c,d,e,f,g = symbols ('a b c d e f g')

#Coordonn�es des points 
M1=[0    ,0    ,0   ]
M2=[a    ,0    ,0 ]
M3=[0  ,-b    ,0 ]

#Ne pas oublier de rajouter les inconnues nulles et autres informations qu'on a � l'endroit pr�cis� ci-dessous

#Param�trage fini on peut lancer le programme


# Repere :
Ro = CoordSys3D('Ro')

# Vecteur des positions des points d'actions de contact par rapport � Rg (i,j,k) de tous les points :
GM1 =  M1[0]*Ro.i  +M1[1]*Ro.j   +M1[2]*Ro.k
GM2 =  M2[0]*Ro.i  +M2[1]*Ro.j   +M2[2]*Ro.k
GM3 =  M3[0]*Ro.i  +M3[1]*Ro.j   +M3[2]*Ro.k

# On d�fini les composantes inconnues des actions de contact de tous les points m�me ceux qu'on connait :
X1,Y1,Z1 = symbols ('X_1 Y_1 Z_1')
X2,Y2,Z2 = symbols ('X_2 Y_2 Z_2')
X3,Y3,Z3 = symbols ('X_3 Y_3 Z_3')

#AJOUTER LES RELATIONS QU'ON CONNAIT DEJA ICI :
Z1=Z2=Z3=0

# On d�fini les r�sultantes des actions m�caniques par rapport � i,j,k de tous les points
R1 = X1*Ro.i   + Y1*Ro.j    + Z1*Ro.k
R2 = X2*Ro.i   + Y2*Ro.j    + Z2*Ro.k
R3 = X3*Ro.i   + Y3*Ro.j    + Z3*Ro.k

# La r�sultant du PFS ->
RPFS  = R1 + R2 + R3

# Le moment r�sultant du PFS -> equation vectorielle
# On passe par les �quations vectorielles pour calculer les moments automatiquement
# avec le produit vectoriel : .cross() -> une des m�todes des objets vecteurs de sympy.

MPFS = GM1.cross(R1) + GM2.cross(R2) + GM3.cross(R3)

# Ici on calcule les �quations scalaires du PFS
# en projetant les �quations vectorielles sur les axes
# du rep�re -> on utilise le produit scalaire .dot()
PFS = []
for unit_vector in Ro.base_vectors():
    PFS.append(RPFS.dot(unit_vector))
for unit_vector in Ro.base_vectors():
    PFS.append(MPFS.dot(unit_vector))


# On r�sout symboliquement le syst�me de 12 �quations et 12 inconnues :
Sol = solve(PFS,[X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3])

# Affichage des solutions :
display(Latex('$'+latex(Sol)+'$'))
