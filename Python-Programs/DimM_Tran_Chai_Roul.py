import numpy as np

#Pignon 1 et pignon 2


C0 = 0.406 #Distance au centre désirée [m]
p = 0.0127 #Pas de chaîne [m]
z1 = 15 #Nombre de dents du pignon menant [-]
z2 = 15 #Nombre de dents du pignon mené [-]

DP1 = p/np.sin(np.pi/z1) #Diamètre primitif du pignon menant [m]
DP2 = p/np.sin(np.pi/z2) #Diamètre primitif du pignon mené [m]


if DP1==DP2 :
  X0 = 2*C0/p+(z1+z2)/2 #Nombre de maillons de chaîne requis [-]
  δ=np.arcsin((DP2-DP1)/(2*C))
  F=1/(4*np.sin(δ)*(δ+1/np.tan(δ)))
  C=(X0*p-DP1*np.pi)/2
  β=2*np.arccos((DP2-DP1)/(2*C))*180/np.pi
  Zc=z1*β/360 

  print('Diamètre P1 = %8.2f mm\t Diamètre P2 = %8.2f mm\n'%(DP1*1000,DP2*1000))
  print('Nombre de maillons nécessaires X0 = %8.2f\n'%(X0))
  print('Entraxe réel nécessaire = %8.2f mm\n'%(C*1000))
  print('Angle de contact β = %8.2f degrés\t Distance actuelle = %8.2f mm\n'%(β,C0*1000))

else :
  X0 = 2*C0/p+(z1+z2)/2+(p*((abs(z2-z1))/(2*np.pi))**2)/C0 #Nombre de maillons de chaîne requis [-]
  δ=np.arcsin((DP2-DP1)/(2*C))
  F=1/(4*np.sin(δ)*(δ+1/np.tan(δ)))
  C=F*p*(2*X0-(z1+z2))
  β=2*np.arccos((DP2-DP1)/(2*C))*180/np.pi
  Zc=z1*β/360 

  print('Diamètre P1 = %8.2f mm\t Diamètre P2 = %8.2f mm\n'%(DP1*1000,DP2*1000))
  print('Nombre de maillons nécessaires X0 = %8.2f\n'%(X0))
  print('Entraxe réel nécessaire = %8.2f mm\n'%(C*1000))
  print('Angle de contact β = %8.2f degrés\t Distance actuelle = %8.2f mm\n'%(β,C0*1000))