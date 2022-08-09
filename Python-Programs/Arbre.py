# A executer En 1er et au début, charge les modules externes nécessaires
import numpy as np               # calculs scientifiques et tableaux multi-dimensionnels
import matplotlib.pyplot as plt  # tracé de courbes
from math import*
import urllib.request
from google.colab import files
%config InlineBackend.figure_format = 'png'

# A noter on donne l'adresse du fichier au format "raw" sur Git
url1 ="https://git.utt.fr/lafon/mecapy/-/raw/master/TraceGrapheCohesion.py"
url2 ="https://git.utt.fr/lafon/mecapy/-/raw/master/Kt_Arbres.py"
TraceGrapheCohesion = urllib.request.urlopen(url1).read().decode()
Kt_Arbres = urllib.request.urlopen(url2).read().decode()
exec(TraceGrapheCohesion,globals())
exec(Kt_Arbres,globals())




######## PRECONFIGURATIONS FORCES
Ft1 = -31000          #Force agissant sur le pignon de gauche si il y a 
Ft2 =   1     #Force agissant sur le pignon de droite si il y a   
a  = 30             #1ère partie
b  = 15            #2ème partie
c  = 15            #3ème partie
R1 = 0           #Rayon pignon 1 si il y a  
R2 = 1             #Rayon pignon 2 si il y a  
b1 = 1             #largeur pignon 1 si il y a  
b2 = 1             #largeur pignon 2 si il y a 

#Forces sur les roulements / ecriture des résultats
XC = 0
YC = Ft2*c/(a+b+c) - Ft1*(b+c)/(a+b+c)
ZC = 0
XD = 0
YD = -Ft1*a/(a+b+c) + Ft2*(a+b)/(a+b+c)
ZD = 0
print('XC = %6.0f N\tYC = %6.0f N\tZC = %6.0f N'%(XC,YC,ZC))
print('XD = %6.0f N\tYD = %6.0f N\tZD = %6.0f N'%(XD,YD,ZD))

#Expression des moments en fonction des sections
expr  = {'Ty' :(lambda x:  -YC,       lambda x: -YC-Ft1,                  lambda x: YD)             ,
         'Mt' :(lambda x:  -2*Ft1*R1,        lambda x: -2*Ft1*R1,                   lambda x: -2*Ft1*R1)             ,
         'Mfz':(lambda x:  (YC*x),    lambda x: YC*x+Ft1*(x)+Ft1*(-a),    lambda x: (-YD*x-YD*(-a-b-c)))
 }

inter = ((0,a),(a,a+b),(a+b,a+b+c))
TraceGrapheCohesion((12,8),100,inter,expr)


#@title  { form-width: "10px" }
######## PRECONFIGURATIONS MATERIAU
Rm = 410         #Rm matériau
Re = 240  
Ks = 1             #Ks définit par rapport à la rugosité et Rm
Ke = 0.9          #Ke définit par rapport à d   

#Determination des deux coef on prend sur le diagramme bleu, Kf/Kt.
coeff = 0.75     #Kff = coeff x Ktf  Donc on prend Ktf et Rm on lit sur la courbre le coeff ////pareil pour coefo ( Kfo = coefo x Kto)
coefo = 0.85  

#Type de rotation : continue/alternée
rotation = 'continue'

#Calcul de SigD0 automatique en fonction de Rm
if (Rm < 800) :
  SigD0 = Rm*(0.56-Rm*1.4e-4)
if (801< Rm < 1300) :
  SigD0 = Rm*(0.57-Rm*1.2e-4)
if (1301< Rm < 3000) :
  SigD0 = Rm*(0.56-Rm*1.4e-4)

######## PRECONFIGURATIONS NOMBRES DE CAS, INTERVALLES, PARAMETRES
#On définit le nombre de cas 
nb=1

#On définit chaque ca, le première cas étant la première colonne (colonne 1 = n°0)
#Cas où on a un  'épaulement'                     #Arbre_epaule(r, d, D) / Arbre_epaule0(dD, rt)
#Cas où on a une 'gorge'                          #Arbre_gorge(r, d, D)  / Arbre_gorge0(dD, rt)
#Cas où on a un  'creux gorge'                    #Arbre_creux_gorge(r, d, D, Di) / Arbre_creux_gorge0(ta, rt)
#Cas où on a un  'creux trou transversal'         #Arbre_creux_gorge(r, d, D, Di) / Arbre_creux_gorge0(ta, rt
cas = ['épaulement', 'épaulement' , 'épaulement', 'épaulement']
#     cas0,cas 1,cas2,cas3

#Emplacement de la section intervalles de 0 à 3 (le premier intervalle est le 0)
# PARAMETRES de chaque endroit étudié, toujours pareil la première colonne c'est le premier cas (n°0)
#        a   : diamètre trou transversal en [mm]
#        r   : rayon gorge/épaulement en [mm] 
#        d   : diamètre fond de gorge en [mm]        
#        D   : diamètre extérieur en [mm]
#        Di  : diamètre du creux en [mm]          
#        dD  : ratio d/D
#        rt  : ration r/t avec t = (D-d)/2
#        ta  : ratio t/a avec t=(D-d)/2 et a=(d-Dint)/2
#        DiD : ratio Di/D null si arbre plein.

#Zone à remplir
intervalles =   [0      ,1       ,1       ,2        ]
abscisses   =   [5.5    ,1+b1/2  ,a+b-b2/2,a+b+c-5.5]
A =             [5      ,5       ,5       , 5       ]
r =             [1      ,1       ,1       , 1       ]
d =             [11     ,11      ,11      ,11       ]                                                                                          
D =             [11.1   ,11.1    ,11.1    ,11.1     ]
Dint =          [11.05  ,11.05   ,11.05   ,11.05    ]
Sens =          [1      ,1       ,-1      ,-1       ] 

#Choix du coeff de statique pour tracé de l'arbre à la fin
Coeffsécurité = 1.5

#Le paramétrage est fini on peut lancer le programme





#Calculs automatiques 
t =     [round((D[0]-d[0])/2,5),round((D[1]-d[1])/2,5),round((D[2]-d[2])/2,5),round((D[3]-d[3])/2,5)]
rt =    [round((r[0]/t[0]),5),round((r[1]/t[1]),5),round((r[2]/t[2]),5),round((r[3]/t[3]),5)]
dD =    [round((d[0]/D[0]),5),round((d[1]/D[1]),5),round((d[2]/D[2]),5),round((d[3]/D[3]),5)]
ta =    [abs(round((2*t[0])/(d[0]-Dint[0]),5)),abs(round((2*t[1]/(d[1]-Dint[1])),5)),abs(round((2*t[2]/(d[2]-Dint[2])),5)),abs(round((2*t[3]/(d[3]-Dint[3])),5))]
DintD = [round((Dint[0]/d[0]), 5),round((Dint[1]/d[1]), 5),round((Dint[2]/d[2]), 5),round((Dint[3]/d[3]), 5)]
AD =    [round((A[0]*D[0]), 2),round((A[1]*D[1]), 2),round((A[2]*D[2]), 2),round((A[3]*D[3]), 2)]

#Affichage des tableaux référençant toutes les valeurs pour chaque cas utilisés uniquement, arrondies à 5 chiffres si besoin est.
print("A     =",A[0:nb:1])
print("r     =",r[0:nb:1])
print("d     =",d[0:nb:1])
print("D     =",D[0:nb:1])
print("Dint  =",Dint[0:nb:1])
print("t     =",t[0:nb:1])
print("rt    =",rt[0:nb:1])
print("dD    =",dD[0:nb:1])
print("ta    =",ta[0:nb:1])
print("DintD =",DintD[0:nb:1])
print("AD    =",AD[0:nb:1])

#Initialisation des tableaux de valeurs, qui vont servir plus tard
Mfcas=[]
Sigfmax=[]
taumax=[]
sigeqcor_casmax=[]
SS=[]
sigeq_a_max=[]
sigeq_m_max=[]
sig_D_max=[]
sigDeq1=[]
Rmeq1=[]
sigD1=[]
sig_a_adm_max=[]
SD_max=[]

#Initialisation de i qui va servir pour la boucle, on le fait tourner jusqu'à qu'il arrive au nombre de cas souhaités
i=0

while (i<nb) :

  print(' ')
  print(' ')
  print(' ')
  print('On se place sur le cas numéro %0.f (voir coordonnées plus haut)'%(i))
  
  #On trouve la valeur Ty,Mt,Mfz pour chaque cas considéré, on voit l'utilité des tableaux là
  Tycas  = expr['Ty'][intervalles[i]](abscisses[i])
  Mtcas  = expr['Mt'][intervalles[i]](abscisses[i])
  Mfzcas = expr['Mfz'][intervalles[i]](abscisses[i])
  Mfycas = 0
  print('Ty %0.f = %0.f N\t Mt %0.f = %0.f N.mm\t Mfz %0.f = %0.f N.mm'%(i,Tycas,i,Mtcas,i,Mfzcas))

  #4 boucles if à la suite pour répondre au choix des cas spécifiques à chaque section (modulaire facilement)
  if (cas[i]=='épaulement'):
    print('épaulement')
    Kt = Arbre_epaule(r[i],d[i],D[i])
    [Ktt,Ktf,Kto] = Arbre_epaule0(dD[i],rt[i])

  if (cas[i]=='gorge'):
    print('gorge')
    Kt  = Arbre_gorge(r[i], d[i], D[i])
    [Ktt,Ktf,Kto] = Arbre_gorge0(dD[i], rt[i])

  if (cas[i]=='creux gorge'):
    print('creux gorge')
    Kt = Arbre_creux_gorge(r[i], d[i], D[i], Dint[i])
    [Ktt,Ktf,Kto] = Arbre_creux_gorge0(ta[i], rt[i])

  if (cas[i]=='creux trou transversal'):
    print('creux trou transversal')
    Kt = Arbre_creux_trou_transversal(A[i], D[i], Dint[i])
    [Ktt,Ktf,Kto] = Arbre_creux_trou_transversal0(AD[i], DintD[i])

  #On affiche les résultats du cas qui nous a servi uniquement donc un seul print avec le numéro de cas affiché (i)
  print("Kt prend la valeur",Kt)
  print('Ktt %0.f = %.5f \t Ktf %0.f = %.5f \t Kto %0.f = %.5f '%(i,Ktt,i,Ktf,i,Kto))

  #Pour chaque valeur trouvée ci dessous on l'ajoute dans les tableaux créés précédement
  #La fonction valeur.append(X) ajoute la valeur X au tableau de nom "valeur"

#Contraintes max liée à la flexion
  Mfcas1 = np.sqrt(Mfycas**2 + Mfzcas**2)
  Mfcas.append(round((Mfcas1),2))
  Sigfmax1 = (d[i]/(2*np.pi*d[i]**4/64))*Mfcas1
  Sigfmax.append(round((Sigfmax1),2))
  print('Sig_flex_max',Sigfmax1)

#Contraintes max liée à la torsion
  taumax1 =  (d[i]/(4*np.pi*d[i]**4/64))*np.abs(Mtcas)
  taumax.append(round((taumax1),2))
  print('Tau_max :',taumax1)

#Contraintes corrigées, alternées et moyennes
  sigeqcor_cas1 = np.sqrt((Ktf*Sigfmax1)**2 + 3*(Kto*taumax1)**2)
  sigeqcor_casmax.append(round((sigeqcor_cas1),2))  
  print('Sig_eq_cor :',sigeqcor_cas1)
  
  #Calcul des Kff et Kfo
  Kff = coeff*Ktf                                                                                                        
  Kfo = coefo*Kto                                                                                                        

  if (rotation=='continue'): #Continue
    sigeq_a = Sigfmax1
    sigeq_a_max.append(round((sigeq_a),2))
    print('Sig_eq_alt :',sigeq_a)
    sigeq_m = taumax1
    sigeq_m_max.append(round((sigeq_m),2))
    print('Sig_eq_moy :',sigeq_m)
    Kfeq = Kff
    Kteq = np.sqrt(3*((taumax1/sigeq_m)*Kto)**2)
    print('Kfeq1 : %.3f\tKteq1 : %.3f'%(Kfeq,Kteq))

  if (rotation=='alternée'): #Alternée 0 à max
    sigeq_a = (np.sqrt((Sigfmax1)**2+3*(taumax1/2)**2))/2
    sigeq_a_max.append(round((sigeq_a),2))
    print('Sig_eq_alt :',sigeq_a)
    sigeq_m = (np.sqrt(3*(taumax1/2)**2))/2
    sigeq_m_max.append(round((sigeq_m),2))
    print('Sig_eq_moy :',sigeq_m)
    Kfeq = np.sqrt(((Sigfmax1/sigeq_a)*Kff)**2+3*((taumax1/sigeq_a)*Kfo/2)**2)
    Kteq = np.sqrt(3*((taumax1/sigeq_m)*Kto/2)**2)
    print('Kfeq1 : %.3f\tKteq1 : %.3f'%(Kfeq,Kteq))


#Calcul Rmeq
  Rmeq = Rm/Kteq
  Rmeq1.append(round((Rmeq),2))

#Coefficient de sécurité en statique
  SS1 = Rmeq/sigeqcor_cas1
  SS.append(round((SS1),2))
  print('Coef. sécu. en statique S_S : %.2f'%SS1)

# Coef de sécurité en fatigue directement
  sigD = (0.9*SigD0*Ke*Ks)
  sigD1.append(round((sigD),2))
  sigDeq =sigD/Kfeq
  sigDeq1.append(round((sigDeq),2))
  sig_a_adm = sigDeq - sigDeq/(2*Rmeq - sigDeq)*sigeq_m
  sig_a_adm_max.append(round((sig_a_adm),2))
  print('Contrainte alternée admissible :',sig_a_adm)
  SD = sig_a_adm/sigeq_a
  SD_max.append(round((SD),2))
  print('Coef. sécu. en fatigue S_D :',SD)

  #On incrémente le i pour repartir pour un tour
  i=1+i

print("  ")
print("  ")

#Préparation pour la construction de diagramme de Haigh de l'état de contrainte de fatigue
#On print chaque tableau complet
print("Mf                =",Mfcas)
print("Sigfmax           =",Sigfmax)
print("taumax            =",taumax)
print("sigeqcor          =",sigeqcor_casmax)
print("SS                =",SS)
print("sigeq_a           =",sigeq_a_max)
print("sigeq_m           =",sigeq_m_max)
print("Rmeq              =",Rmeq1)
print("sigD              =",sigD1)
print("sigDeq            =",sigDeq1)
print("sig_a_adm         =",sig_a_adm_max)
print("SD                =",SD_max)
print("  ")
print("  ")

#On trouve la section critique et on affiche chaque résultat dans cette section critique pour voir ce qu'il faut changer
section_critique=SD_max.index(min(SD_max))
print("section critique",section_critique)
print("  ")
print("A                 =",A[section_critique])
print("r                 =",r[section_critique])
print("d                 =",d[section_critique])
print("D                 =",D[section_critique])
print("Dint              =",Dint[section_critique])
print("  ")
print("Mf                =",Mfcas[section_critique])
print("Sigfmax           =",Sigfmax[section_critique])
print("taumax            =",taumax[section_critique])
print("sigeqcor          =",sigeqcor_casmax[section_critique])
print("SS                =",SS[section_critique])
print("sigeq_a           =",sigeq_a_max[section_critique])
print("sigeq_m           =",sigeq_m_max[section_critique])
print("Rmeq              =",Rmeq1[section_critique])
print("sigD              =",sigD1[section_critique])
print("sigDeq            =",sigDeq1[section_critique])
print("sig_a_adm         =",sig_a_adm_max[section_critique])
print("SD                =",SD_max[section_critique])
print("  ")
print("  ")

#On trouve le maximum de toutes section confondues
sigDmax = max(sigD1[0:nb:1])
SigDeqmax = max(sigDeq1[0:nb:1])
Rmeqmin = min(Rmeq1[0:nb:1])

#On plot de diagramme de Haigh
plt.figure(figsize=(12,5)) # Création figure 12x5 inch.
# Tracé diagramme sans effet des Kt
plt.plot([0,Rm-sigDmax/2,Rm],[sigDmax,sigDmax/2,0],'r-.',lw=0.5)
# Tracé diagramme avec abattement du aux Kt.
plt.plot([0,Rmeqmin-SigDeqmax/2,Rmeqmin],[SigDeqmax,SigDeqmax/2,0],'r-',lw=2)
plt.fill_between([0,Rmeqmin-SigDeqmax/2,Rmeqmin],[SigDeqmax,SigDeqmax/2,0],color='olive',alpha=0.1)
# Mise en forme ...
plt.xlim(0,1.1*Rm)
plt.ylim(0,1.1*sigDmax)
plt.grid()
plt.xlabel(r'$\sigma_{eq_m}$',fontsize=14)
plt.ylabel(r'$\sigma_{eq_a}$',fontsize=14)
# Point représentant l'état de contraintes :

print("  ")
print("  ")

if (nb>0) :
  plt.plot(sigeq_m_max[0],sigeq_a_max[0],'r*')
  print('Section 0','ROUGE')

if (nb>1) :
  plt.plot(sigeq_m_max[1],sigeq_a_max[1],'b*')
  print('Section 1','BLUE')

if (nb>2) :
  plt.plot(sigeq_m_max[2],sigeq_a_max[2],'g*')
  print('Section 2','GREEN')

if (nb>3) :
  plt.plot(sigeq_m_max[3],sigeq_a_max[3],'y*')
  print('Section 3','YELLOW')



  #Mtn on va plot une courbe qui va tracer le coef minimum de l'arbre
ramin=[]

for i in range (0,a+b+c,1):
  if (0<=i<a):
    Tycas  = expr['Ty'][0](i)
    Mtcas  = expr['Mt'][0](i)
    Mfzcas = expr['Mfz'][0](i)
    Mfycas = 0

    Sigeqcorr = Re/Coeffsécurité
    Mfcas1 = np.sqrt(Mfycas**2 + Mfzcas**2)
    ra=((1/(np.pi**2))*(16*Mfcas1**2+12*(np.abs(Mtcas))**2)*(1/Sigeqcorr)**2)**(1/6)

  if (a<=i<a+b):
    Tycas  = expr['Ty'][1](i)
    Mtcas  = expr['Mt'][1](i)
    Mfzcas = expr['Mfz'][1](i)
    Mfycas = 0

    Sigeqcorr = Re/Coeffsécurité
    Mfcas1 = np.sqrt(Mfycas**2 + Mfzcas**2)
    ra=((1/(np.pi**2))*(16*Mfcas1**2+12*(np.abs(Mtcas))**2)*(1/Sigeqcorr)**2)**(1/6)

  if (a+b<=i<=a+b+c):
    Tycas  = expr['Ty'][2](i)
    Mtcas  = expr['Mt'][2](i)
    Mfzcas = expr['Mfz'][2](i)
    Mfycas = 0

    Sigeqcorr = Re/Coeffsécurité
    Mfcas1 = np.sqrt(Mfycas**2 + Mfzcas**2)
    ra=((1/(np.pi**2))*(16*Mfcas1**2+12*(np.abs(Mtcas))**2)*(1/Sigeqcorr)**2)**(1/6)

  ramin.append(round((ra),2))

plt.figure(figsize=(40,15))
x = np.linspace(0,a+b+c-1,a+b+c)
plt.plot(x,ramin,'rD',linestyle = 'solid', label='Rayon statique minimal pour S=1.5')
plt.xticks(np.arange(0,a+b+c+1,10))
plt.yticks(np.arange(5,30,1))
plt.grid()
plt.xlabel('Largeur arbre en mm',fontsize=25)
plt.ylabel('Rayon minimal arbre en mm',fontsize=25)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.title('Approximation du diamètre minimal de l arbre',fontsize=30)

#On plot les visuels des diamètres attendus sur les arbres
i=0

while (i<nb) : 
  x2=[]
  y1=[]
  for j in range(-2,3,1) :
    x2.append(abscisses[i]+j)
  
  if (Sens[i]==1) :
    y1 = [d[i]/2, d[i]/2, (D[i]+d[i])/4, D[i]/2, D[i]/2]

  if (Sens[i]==-1) :
    y1 = [D[i]/2 , D[i]/2 , (D[i]+d[i])/4 , d[i]/2, d[i]/2]

  plt.plot(x2, y1,'gD',linestyle = 'solid', label='Rayon minimal sections critiques')

  i = 1+i

plt.legend()

# Téléchargement de la courbe
#plt.savefig('rayon_arbre.png',dpi=1000)
#files.download('rayon_arbre.png')


