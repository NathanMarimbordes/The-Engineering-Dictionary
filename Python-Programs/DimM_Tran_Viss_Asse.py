import numpy as np
import matplotlib.pyplot as plt
from math import*

#VIS
d = 6              # Diametre nominal de la vis                     [mm]
p = 1.250               # Pas de la vis (série pas "gros")    
rho2 = 13/2           # Rayon extérieur tête de vis                    [mm]     
rho1 = 9/2         # Rayon extérieur tige                           [mm]


#Matériau
Classe=8
Multiplicateur=8


#COEFFICIENTS
f1 = 0.10            # Coeff vis/pas de vis             
fp = 0.15             # Coeff de frottement tête/pièce
f2 = 0.15            # Coeff pièce/pièce (si il y a deux pièces)
f  = 0.15             # Coeff de frottement vis/pièce (pareil que fp)               
alpha  = 1.5         # Coeff incertitude clé dynamométrique 


#LONGUEURS MAITRESSES
l0      = 1          #Longueur non fileté de la vis                   [mm]                    
l1      = 14         #Longueur de la vis comprise dans la pièce[mm] 
l3      = 14     #Longueur de la vis filetée avant d'arriver à l'écrou [mm] 

lp1     = 4         #Epaisseur traversée dans la pièce 1 par la vis  [mm]
lp2     = 10         #Epaisseur traversée dans la pièce 2 par la vis  [mm]

Dp = 15              #Diamètre de la pièce traversée                   [mm]
Dt = 6.5            #Diamètre trou de la pièce                        [mm]

gamma = 1               # Coef. intro. niv chargement


#SI DEUX PIECES UNIQUEMENT
h1  = 4             #Epaisseur pièce 1
h2  = 10             #Épaisseur pièce 2       
AP1 = 1000           #Section équivalente raideur pièces serrées       [mm^2]
lP1 = 4           #Epaisseur totale de section AP1
h3  = 15             #Épaisseur entretoise/rondelle 1
h4  = 15             #Épaisseur entretoise/rondelle 2    
AP2 = 792.05           #Section équivalente raideur entretoise/rondelle  [mm^2]
lP2 = 60           #Epaisseur totale de section AP2



#CONFIGURATION
J  = 'écrou'        #Type de serrage, J=0.5 serrage par écrou, J=1.5 serrage dans un trou borgne
cas='tangentiel'    #Cas tangentiel // traction // flexion // tang:trac // couplemaxserrage // alternée


#DONNES CONNUES (=0 SI PAS CONNUES)
Cserr   = 20000
FPmini  = 0       #Effort presseur minimal => Mettre 0 si on ne veut pas de décollement
FPmaxi  = 0
FB      = 0
FBmini  = 0
FBmaxi  = 0
FE      = 500      #Mettre 0 Si on veut savoir combien on peut résister avec notre couple de serrage
FEmini  = 0
FEmaxi  = 500
FT      = 7500

FL      = 0
Mf      = 0
m       = 0
n       = 0
Ip      = 0


EB      = 210000     #Module de young du boulon                       [Mpa]
Ep      = 210000     #Module de young de la pièce                     [Mpa]
Ep1     = 210000     #Module de young de la pièce 1                   [Mpa]
Ep2     = 210000     #Module de young de la pièce 2                   [Mpa]

#FINITO TU PEUX LANCER


#Paramétrage fini on peut lancer le programme
Re = Classe*100*Multiplicateur*0.1
Da = rho2*2         #Diamètre tête de vis
rhomoy=0.5*(rho1+rho2)
lp = lp1+lp2        #Epaisseur de l'assemblage 
d2 = d - 0.6495*p   # Diamètre moyen à flanc de filets 
d3 = d - 1.2268*p   # Diamètre du noyaux de la vis 
ds = (d2+d3)/2      # Diamètre section résistante 
K1 = (0.16*p + 0.583*d2*f1)
K2 = f2*(rho2+rho1)/2
As = np.pi*ds**2/4
A0 = np.pi*d**2/4
print('K1  : % 0.3f'%K1)
print('K2  : % 0.3f\n'%K2)
print('As : %0.2f mm2'%As)
print('A0 : %0.2f mm2\n'%A0)
print('ds : %0.2f mm2\n'%ds)

if Dp<(Da-0.001):
    Ap = (np.pi/4)*((Dp**2)-(Dt**2))
    print('Section équivalente : %0.1f mm2\n'%Ap)
if Da<Dp<(Da+lp) and J=='écrou':
  x1 = ((lp*Da)/Dp)**(1/3)
  Ap = (np.pi/4)*((Da**2)-(Dt**2))+(np.pi/8)*Da*(Dp-Da)*x1*(x1+2)
  print('Section équivalente : %0.1f mm2\n'%Ap)
if Da<Dp<(Da+lp) and J=='borgne':
  x1 = ((lp*Da)/Dp)**(1/3)
  Ap = (np.pi/4)*((Da**2)-(Dt**2))+(np.pi/8)*Da*(Dp-Da)*x1*(x1+2)
  print('Section équivalente : %0.1f mm2\n'%Ap)
if Dp>(Da+lp-0.0001) and J=='écrou':
  x1 = ((lp*Da)/((lp+Da)**2))**(1/3)
  Ap = (np.pi/4)*((Da**2)-(Dt**2))+(np.pi/8)*Da*lp*(Dp-Da)*x1*(x1+2)
  print('Section équivalente : %0.1f mm2\n'%Ap)
if Dp>(Da+lp-0.0001) and J=='borgne':
  x1 = (lp/(lp+Da))**(0.2)
  Ap = (np.pi/4)*((Da**2)-(Dt**2))+(np.pi/8)*Da*lp*(Dp-Da)*x1*(x1+2)
  print('Section équivalente : %0.1f mm2\n'%Ap)


####RAJOUTER ICI LES INFOS QUON POURRAIT AVOIR D'IMPOSEES



# DEBUT DES CALCOULS

SP = 1/Ap*(lP1/Ep1 + lP2/Ep2)
KP = 1/SP
SB = ((l0+0.4*d)/A0 + (l1+0.4*d)/As)/EB
KB = 1/SB
Lambda = gamma*KB/(KB+KP)
print('KP : %.3e N/mm'%KP)
print('KB : %.3e N/mm\n'%KB)
print('Lambda : %0.3f\n'%Lambda)

SPA = (3/(3.93*EB))+(19/(122*EB))+(1/(122*3000))+(5/(122*EB))+(1/(122*3000))
KPA = 1/SPA
print('KPA %0.2f\n'%KPA)
print('SPA %0.002f\n'%SPA)

SIGA=6254/(2*As)*1*(KB/(KB+KPA))
print('SIGA %0.2f\n'%SIGA)

if cas=='tangentiel' : 
  print('Cas tangentiel')
  if Cserr==0 :   #Si on veut plot la courbe de l'évolution du Couple de Serrage nécessaire en fonction des données
    FPmini2=[]
    Tc2=[]
    for Cserr in range(0,50000,1000) :
      G = (2*Cserr)/((alpha+1)*(K1+K2))
      FPmini2.append(G)
      Tc2.append(G*f)
    plt.figure(figsize=(30,20))
    plt.xticks(np.arange(0,55000,5000),fontsize=30)
    plt.yticks(np.arange(0,25000,1000),fontsize=30)
    plt.grid()
    plt.xlabel('Cserr [N.m]',fontsize=50)
    plt.ylabel('Effort  [N]',fontsize=50)
    plt.rc('legend', fontsize=30)
    plt.legend()
    x=np.arange(0,50000,1000)
    plt.plot(x,FPmini2,'r',label='Fp mini en fonction de Cserr')
    plt.plot(x,Tc2,'b',label='Ft mini en fonction de Cserr')
    plt.show()

  if FT==0 :    #Si on ne connait pas l'effort tangentiel et qu'on veut trouver le maximum

    FPmini = (2*Cserr)/((alpha+1)*(K1+K2))
    Tc = FPmini*f
    print('FPmini :  %0.f N'%FPmini)
    print('Tc :  %0.f N\n'%Tc)
    F0maxi = 0.9*Re/(np.sqrt( 1/As**2 + 3*(16*K1/(np.pi*ds**3))**2 ) )
    F0mini = F0maxi/alpha
    F0moy = 0.5*(F0mini+F0maxi)
    print('F0maxi : %0.f N'%F0maxi)
    print('F0mini : %0.f N'%F0mini)
    print('F0moy  : %0.f N\n'%F0moy)
    CserrMaxi = F0maxi*(K1+K2)*(alpha+1)/(2*alpha)
    TcMax = (F0maxi*f)/(alpha)
    print('Cserr choisi  : %0.2f N.m'%(Cserr*1e-3))
    print('CserrMaxi :  %0.2f N.m'%(CserrMaxi*1e-3))
    print('TcMax :  %0.f N\n'%TcMax)

  #if FT!=0 :  #Si on connait l'effort tangentiel et qu'on veut trouver le Couple de serrage correspondant nécessaire
    F0maxi=TcMax*alpha/f
    CserrMaxi = F0maxi*(K1+K2)*(alpha+1)/(2*alpha)
    F0mini = F0maxi/alpha
    F0moy = 0.5*(F0mini+F0maxi)
    FPmini = FT/f
    Cserr = FPmini*((alpha+1)*(K1+K2))/2

    print('Tc :  %0.f N\n'%Tc)    
    print('FPmini :  %0.f N'%FPmini)

    print('F0maxi : %0.f N'%F0maxi)
    print('F0mini : %0.f N'%F0mini)
    print('F0moy  : %0.f N\n'%F0moy)
    print('Cserr choisi  : %0.2f N.m'%(Cserr*1e-3))
    print('CserrMaxi :  %0.2f N.m'%(CserrMaxi*1e-3))
    

if cas=='traction':
  print('Cas Traction')

  if FE!=0:
    F0mini = (1-Lambda)*FE
    F0maxi = alpha*F0mini
    FBmaxi = F0maxi + Lambda*FE
    Sig = FBmaxi/As
    Tau =  (16*K1*F0maxi)/(np.pi*ds**3)
    SigVM = np.sqrt(Sig**2 + 3*Tau**2)

    print('FBmaxi    : %0.f N\n'%FBmaxi)
    print('F0maxi :  %0.f N'%F0maxi)
    print('F0mini :  %0.f N'%F0mini)
    print('Sig    : %0.f MPa'%Sig)
    print('Tau    : %0.f MPa'%Tau)
    print('SigVM  : %0.f MPa\n'%SigVM)

    #Affichage visuel de Lambda et 0.9*Re
    def FSigVM(x):
        F0mini = (1-x)*FE
        F0maxi = alpha*F0mini
        FBmaxi =  F0maxi + x*FE  
        Sig = FBmaxi/As
        Tau = (16*K1*F0maxi)/(np.pi*ds**3)    
        SigVM = np.sqrt(Sig**2 + 3*Tau**2) 
        return SigVM

    x=np.linspace(0.1,1,100)
    plt.figure(figsize=(30,15))
    plt.plot(x,FSigVM(x),'r-',label=r'$\sigma_{eq}(\lambda)$')
    plt.plot([0.1,1],[0.9*Re,0.9*Re],'b-',label=r'$0.9R_e=576$ MPa')
    plt.plot([0.1,1],[FSigVM(0.1),FSigVM(1)],'g-.',label='Approx. linéaire')
    plt.legend()
    plt.grid()
    
    #Calcul exact de Lambda et SigVm
    test=[]
    for x in range(0,500,1) :
      F0mini = (1-(0.001*x))*FE
      F0maxi = alpha*F0mini
      FBmaxi =  F0maxi + (0.001*x)*FE  
      Sig = FBmaxi/As
      Tau = (16*K1*F0maxi)/(np.pi*ds**3)    
      SigVM = np.sqrt(Sig**2 + 3*Tau**2) 
      if 0.99*0.9*Re<SigVM<1.01*0.9*Re:
        test.append(x)
    valeur = sum(test)/len(test)
    print('Lambda exact : %0.3f'%(valeur*1e-3))
    SigVMexact=FSigVM((valeur*1e-3))
    print('SigVMexact : %0.2f\n'%SigVMexact)

  if FPmini==0 : 
    print('Calcul pour éviter le décollement en fonction de FE \n')
    F0mini = FE*(KP/(KB+KP))
    F0max = F0mini*alpha
    F0moy = 0.5*(F0mini+F0maxi)
    print('F0Mini : %0.f N'%F0mini)
    print('F0Moy  : %0.f N'%F0moy)
    print('F0Maxi : %0.f N'%F0maxi)
    Cserr2 = F0moy*(K1+K2)
    print('Cserr  : %0.2f N.m\n'%(Cserr2*1e-3))

  if FE==0 :  #On veut savoir les efforts extérieurs qu'on peut supporter avec un couple de serrage 
    print('FE max supportable avec Cserr = %.f Nm \n'%Cserr)
    F0moy = Cserr/(K1+K2)
    FE = F0moy/(KP/(KB+KP))

    print('F0Moy  : %0.f N'%F0moy)
    print('FEmax  : %0.f N'%FE)
    print('Cserr  : %0.2f N.m\n'%(Cserr*1e-3))


if cas=='tang:trac':
  print('Cas tangentiel/traction')

  SP = 1/Ap*(lP1/Ep1 + lP2/Ep2)
  KP = 1/SP
  SB = ((l0+0.4*d)/A0 + (l3+0.4*d)/As)/EB
  KB = 1/SB
  gamma = lP1/(lP1+lP2)
  Lambda = gamma*KB/(KB+KP)
  print('KP : %.3e N/mm'%KP)
  print('KB : %.3e N/mm\n'%KB)
  print('Lambda : %0.3f\n'%Lambda)
  print('Gamma  : %0.3f'%gamma)

  SigAlt = Lambda/(2*As)*(FEmaxi - FEmini)
  print('SigAlt : %0.f MPa\n'%SigAlt)

  #Variation de lambda en fonction de l'épaisseur de la pièce
  FKP = lambda h : Ep/(lP1/AP1 + 2*h/AP2)
  FKB = lambda h : EB/((l0+0.4*d)/A0 + (2*(h1+h)-l0+0.4*d)/As)
  FGamma = lambda h : h1/(h1+h)
  FLambda = lambda h : FGamma(h)*FKB(h)/(FKB(h)+FKP(h))
  h=np.linspace(0,40,100)
  plt.plot(h,FLambda(h),'r-')
  plt.grid() 

  FPmini = FT/fp
  print('FPMini : %0.f N\n'%FPmini)

  F0mini = FPmini + (1-Lambda)*FEmaxi
  F0maxi = alpha*F0mini
  print('F0mini : %0.f N'%F0mini)
  print('F0maxi : %0.f N\n'%F0maxi)

  FBmaxi = F0maxi + Lambda*FEmaxi
  print('FBmaxi : %0.f N\n'%FBmaxi)

  Sigmax = FBmaxi/As
  Taumax = (16*K1*F0maxi)/(np.pi*ds**3)
  SigVM_max=np.sqrt(Sigmax**2 + 3*Taumax**2)
  print('K1 : %0.3fmm\n'%K1)
  print('Sigmax    : %0.f MPa'%Sigmax)
  print('Taumax    : %0.f MPa'%Taumax)
  print('SigVM_max : %0.f MPa\n'%SigVM_max)

  Remini = SigVM_max/0.9
  print('ReMini : %.0f MPa\n'%Remini)

  Cserr = (F0maxi+F0mini)/2*(K1+K2)
  print('Cserr  : %.2f N.m\n'%(Cserr*1e-3))

 

  #Calcul comparaison contrainte équivalente fonction de Fomax  
  plt.figure(figsize=(50,20))
  x2 = np.linspace(0,10000,1000)

  g       = 1          #Coefficient de déport de charge
  l       = (g*KB)/(KB+KP)
  F0moy   = FPmini+(1-l)*FEmini
  FB      = FPmini+x2
  K1      = 0.16*p+0.583*(d-0.6495*p)*f1
  sigf    = (16*K1*F0moy)/(np.pi*(ds**3))
  tau     = FB/As
  S       = np.sqrt(sigf**2 + 3*tau**2)
  #Lambda = gamma*KB/(KB+KP)


  S= np.linspace(0,10000,1000)
  x=[3,4,4,5,5,6,6,6,8,10,12,14]
  y=[ 6,6,8,6,8,6,8,9,8,9,9,9]
  for i in range(0,len(x)):
    X=x[i] 
    Y=y[i]
    Remin  = np.linspace(0.9*X*Y*10,0.9*X*Y*10,1000)
    print('0.9*Re_mini_%1.0f:%1.0f = %6.0f Mpa'%(X,Y,0.9*X*Y*10))
    couleur=['b','g','r','c','m','y','k','tab:orange','tab:brown','tab:pink','tab:olive','tab:cyan'] 
    #{'tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan'}
    plt.plot(x2,Remin,couleur[i],linestyle = 'solid', label=['Remin',x[i],y[i]])

  plt.plot(x2,S,'r',linestyle = 'solid', label='S_eq',linewidth=5)
  plt.xticks(np.arange(0,10000,1000),fontsize=30)
  plt.yticks(np.arange(0,2000,1000),fontsize=30)
  plt.grid()
  plt.xlabel('Réaction R entre les pignons [N]',fontsize=50)
  plt.ylabel('Contrainte équivalente  [Mpa]',fontsize=50)
  #plt.title('Evolution de la contrainte équivalente en fonction de la réaction R', fontsize=50)
  plt.rc('legend', fontsize=30)
  plt.legend()
  plt.show()

if cas=='flexion':
  print('Cas flexion')
  if FE!=0 : #Calcul comparaison contrainte équivalente fonction de Fomax  
    plt.figure(figsize=(50,20))
    x2 = np.linspace(0,100,10)

    F0moy   = FPmini+(1-Lambda)*FEmini

    DeltaP = (FL/KP)*(1+m*n*(Ap/Ip))
    λex = gamma*((KB*(1+m*n*(Ap/Ip)))/(KP+KB*(1+n*n*Ap/Ip)))
    MFB = (KB/KP)*(n*F0moy+(m+n*λex)*FE)
    Sigtmax = FL/As
    Sigfmax = (32*MFB)/(np.pi*ds**3)
    Taumax = 16*F0moy*K1/(np.pi*ds**3)
    Sigeq = sqrt((Sigtmax + Sigfmax)**2+3*Taumax**2)

    print('Déplacement : %0.f mm'%DeltaP)
    print('λex : %0.f mm'%λex)
    print('MFB  : %0.f Nmm\n'%MFB)
    print('Sigtmax  : %0.f N/mm2'%Sigtmax)
    print('Sigfmax  : %0.f N/mm2'%Sigfmax)
    print('Taumax  : %0.f N/mm2'%Taumax)
    print('Sigeq  : %0.f N/mm2\n'%Sigeq)

    ΔFE = FEmaxi-FEmini
    ΔFB = λex*ΔFE
    ΔMFB = (KB/KP)*(m+n*λex)*ΔFE
    σa=λex*ΔFE/(2*As)+(ΔMFB*ds)/(4*Ip)

    print('ΔFE  : %0.f N'%ΔFE)
    print('ΔFB  : %0.f N'%ΔFB)
    print('ΔMFB  : %0.f Nmm'%ΔMFB)
    print('σa  : %0.f N/mm2\n'%σa)

  if FE==0 :
    x=[3,4,4,5,5,6,6,6,8,10,12,14]
    y=[ 6,6,8,6,8,6,8,9,8,9,9,9]


    for i in range(0,len(x)):
      X=x[i] 
      Y=y[i]
      Remin  = np.linspace(0.9*X*Y*10,0.9*X*Y*10,10)
      print('0.9*Re_mini_%1.0f:%1.0f = %6.0f Mpa'%(X,Y,0.9*X*Y*10))
      couleur=['b','g','r','c','m','y','k','tab:orange','tab:brown','tab:pink','tab:olive','tab:cyan'] 
      #{'tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan'}
      plt.plot(x2,Remin,couleur[i],linestyle = 'solid', label=['Remin',x[i],y[i]],linewidth=5)

    plt.plot(x2,S,'r',linestyle = 'solid', label='S_eq',linewidth=5)
    plt.xticks(np.arange(0,100,10),fontsize=30)
    plt.yticks(np.arange(0,1200,50),fontsize=30)
    plt.grid()
    plt.xlabel('Couple moteur [N.m]',fontsize=50)
    plt.ylabel('Contrainte équivalente  [Mpa]',fontsize=50)
    #plt.title('Evolution de la contrainte équivalente en fonction de la réaction R', fontsize=50)
    plt.rc('legend', fontsize=30)
    plt.legend()
    plt.show()

    #Couple de serrage
    plt.figure(figsize=(50,20))
    x = np.linspace(0,100,2)
    y = [Cserr*(10**-3),Cserr*(10**-3)]
    plt.plot(x,y,'b',linestyle = 'solid', label='Couple de serrage minimum [N.m]',linewidth=5) #Attention penser à changer rho1 et rho2 si on veut le Cserr
    plt.xticks(np.arange(0,100,5),fontsize=30)
    plt.yticks(np.arange(0,10,1),fontsize=30)
    plt.grid()
    plt.xlabel('Force tangentielle exercée',fontsize=50)
    plt.ylabel('Couple de serrage minimum  [N.m]',fontsize=50)
    plt.rc('legend', fontsize=30)
    plt.legend()
    plt.show()

if cas!='rien': #CALCUL COUPLE SERRAGE EN FONCTION DE LA CLASSE
  print('Cserr max en fonction de F0 précédent')
  F0maxi = 0.9*Re/(np.sqrt( 1/As**2 + 3*(16*K1/(np.pi*ds**3))**2 ))
  F0mini = F0maxi/alpha
  F0moy = 0.5*(F0mini+F0maxi)
  Cserr = F0moy*(K1+K2)
  print('F0Maxi : %0.f N'%F0maxi)
  print('F0Mini : %0.f N'%F0mini)
  print('F0Moy  : %0.f N'%F0moy)
  print('Cserr  : %0.2f N.m\n'%(Cserr*1e-3))

  if Classe==0 and Multiplicateur==0 :
    x=[3,4,4,5,5,6,6,6,8,10,12,14]                 #Premier chiffre de la qualité 
    y=[ 6,6,8,6,8,6,8,9,8,9,9,9]                   #Deuxième chiffre de la qualité
    for i in (0,1,2,3,4,5,6,7,8,9,10,11) :
        Re = x[i]*100*y[i]*0.1
        B =((0.9*Re/(np.sqrt( 1/As**2 + 3*(16*K1/(np.pi*ds**3))**2 ) ))*(K1+K2)*(alpha+1)/(2*alpha))*1e-3
        print('Cserr max %.f.%.f = %6.0f N.m'%(x[i],y[i],B))

if cas=='alternée' : 
  print('Cas alternée')



