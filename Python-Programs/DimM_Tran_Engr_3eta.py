#Initialisation valeurs
amin1 = 1e40
amin3 = 1e40
amin5 = 1e40
Z2max = 1e40
Z4max = 1e40
Z6max = 1e40

for im1,m1 in enumerate(modules):
    b1 = largeurs[im1]
    for Z1 in dentures:
        Sig1 = (11*C1)/(b1*m1**2*Z1)
        if (Sig1<=SigFlim):
          for Z2 in dentures2:
            if Z1<Z2 :
              Sig2 = (11*C1*Z2/Z1)/(b1*m1**2*Z2)
              if (Sig2<=SigFlim):
                a1=m1*(Z1+Z2)/2
                for im3,m3 in enumerate(modules):
                    b3 = largeurs[im3]
                    for Z3 in dentures:
                        Sig3 = (11*C1*Z2/Z1)/(b3*m3**2*Z3)
                        if (Sig3<=SigFlim):
                          for Z4 in dentures2:
                            if Z3<Z4 :
                              Sig4 = (11*C1*Z4*Z2/(Z1*Z3))/(b3*m3**2*Z4)
                              if (Sig4<=SigFlim):
                                a3=m3*(Z3+Z4)/2
                                for im5,m5 in enumerate(modules):
                                  b5 = largeurs[im5]
                                  for Z5 in dentures:
                                      Sig5 = (11*C1*Z5/Z3)/(b5*m5**2*Z5)
                                      if (Sig5<=SigFlim):
                                        for Z6 in dentures2:
                                          if Z5<Z6 :
                                            Sig6 = (11*C1*Z4*Z6/(Z3*Z5))/(b5*m5**2*Z6)
                                            if (Sig6<=SigFlim):
                                              a5=m5*(Z5+Z6)/2
                                              if (imoins)<(Z1*Z3*Z5)/(Z2*Z4*Z6)<(iplus):
                                                  if Choix=='a1':
                                                    if a1<amin1 :
                                                      amin1=a1
                                                      i1 = Z1/Z2
                                                      i2 = Z3/Z4
                                                      i3 = Z5/Z6
                                                      itotal = i1*i2*i3
                                                      print(' *** Entraxe étage 1 : %6.2fmm\t Z1 : %d\t Z2 : %d\t Module : %4.2f\t Contrainte 1 : %6.2fMPa\t Contrainte 2 : %6.2fMPa\t i1 : %6.8f'%(a1,Z1,Z2,m1,Sig1,Sig2,i1))
                                                      print(' *** Entraxe étage 2 : %6.2fmm\t Z3 : %d\t Z4 : %d\t Module : %4.2f\t Contrainte 3 : %6.2fMPa\t Contrainte 4 : %6.2fMPa\t i2 : %6.8f'%(a3,Z3,Z4,m3,Sig3,Sig4,i2))
                                                      print(' *** Entraxe étage 3 : %6.2fmm\t Z5 : %d\t Z6 : %d\t Module : %4.2f\t Contrainte 5 : %6.2fMPa\t Contrainte 6 : %6.2fMPa\t i3 : %6.8f'%(a5,Z5,Z6,m5,Sig5,Sig6,i3))
                                                      print('itotal : %6.8f\t iréel : %6.8f'%(itotal,i))
                                                      print("  ")
                                                  if Choix=='a3':
                                                    if a3<amin3 :
                                                      amin3=a3
                                                      i1 = Z1/Z2
                                                      i2 = Z3/Z4
                                                      i3 = Z5/Z6
                                                      itotal = i1*i2*i3
                                                      print(' *** Entraxe étage 1 : %6.2fmm\t Z1 : %d\t Z2 : %d\t Module : %4.2f\t Contrainte 1 : %6.2fMPa\t Contrainte 2 : %6.2fMPa\t i1 : %6.8f'%(a1,Z1,Z2,m1,Sig1,Sig2,i1))
                                                      print(' *** Entraxe étage 2 : %6.2fmm\t Z3 : %d\t Z4 : %d\t Module : %4.2f\t Contrainte 3 : %6.2fMPa\t Contrainte 4 : %6.2fMPa\t i2 : %6.8f'%(a3,Z3,Z4,m3,Sig3,Sig4,i2))
                                                      print(' *** Entraxe étage 3 : %6.2fmm\t Z5 : %d\t Z6 : %d\t Module : %4.2f\t Contrainte 5 : %6.2fMPa\t Contrainte 6 : %6.2fMPa\t i3 : %6.8f'%(a5,Z5,Z6,m5,Sig5,Sig6,i3))
                                                      print('itotal : %6.8f\t iréel : %6.8f'%(itotal,i))
                                                      print("  ")
                                                  if Choix=='DentsZ2':
                                                    if Z2<Z2max :
                                                      Z2max=Z2
                                                      i1 = Z1/Z2
                                                      i2 = Z3/Z4
                                                      i3 = Z5/Z6
                                                      itotal = i1*i2*i3
                                                      print(' *** Entraxe étage 1 : %6.2fmm\t Z1 : %d\t Z2 : %d\t Module : %4.2f\t Contrainte 1 : %6.2fMPa\t Contrainte 2 : %6.2fMPa\t i1 : %6.8f'%(a1,Z1,Z2,m1,Sig1,Sig2,i1))
                                                      print(' *** Entraxe étage 2 : %6.2fmm\t Z3 : %d\t Z4 : %d\t Module : %4.2f\t Contrainte 3 : %6.2fMPa\t Contrainte 4 : %6.2fMPa\t i2 : %6.8f'%(a3,Z3,Z4,m3,Sig3,Sig4,i2))
                                                      print(' *** Entraxe étage 3 : %6.2fmm\t Z5 : %d\t Z6 : %d\t Module : %4.2f\t Contrainte 5 : %6.2fMPa\t Contrainte 6 : %6.2fMPa\t i3 : %6.8f'%(a5,Z5,Z6,m5,Sig5,Sig6,i3))
                                                      print('itotal : %6.8f\t iréel : %6.8f'%(itotal,i))
                                                      print("  ")
                                                  if Choix=='DentsZ4':
                                                    if Z4<Z4max :
                                                      Z4max=Z4    
                                                      i1 = Z1/Z2
                                                      i2 = Z3/Z4
                                                      i3 = Z5/Z6
                                                      itotal = i1*i2*i3
                                                      print(' *** Entraxe étage 1 : %6.2fmm\t Z1 : %d\t Z2 : %d\t Module : %4.2f\t Contrainte 1 : %6.2fMPa\t Contrainte 2 : %6.2fMPa\t i1 : %6.8f'%(a1,Z1,Z2,m1,Sig1,Sig2,i1))
                                                      print(' *** Entraxe étage 2 : %6.2fmm\t Z3 : %d\t Z4 : %d\t Module : %4.2f\t Contrainte 3 : %6.2fMPa\t Contrainte 4 : %6.2fMPa\t i2 : %6.8f'%(a3,Z3,Z4,m3,Sig3,Sig4,i2))
                                                      print(' *** Entraxe étage 3 : %6.2fmm\t Z5 : %d\t Z6 : %d\t Module : %4.2f\t Contrainte 5 : %6.2fMPa\t Contrainte 6 : %6.2fMPa\t i3 : %6.8f'%(a5,Z5,Z6,m5,Sig5,Sig6,i3))
                                                      print('itotal : %6.8f\t iréel : %6.8f'%(itotal,i))
                                                      print("  ")