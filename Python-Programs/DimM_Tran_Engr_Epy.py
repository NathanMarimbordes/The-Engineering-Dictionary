import numpy as np

#Type de cas
Type = '1'
Lambda = 0.8745
Lmin = 0.95*Lambda
Lmax = 1.05*Lambda
k = (1/49)
kmin = 0.98*k
kmax = 1.02*k
m = 1.5
Zmin = 18
Nsat = 3

couronne = np.arange(10,200,1)
pignon = np.arange(Zmin,100,1)

#Initialisation
Z2=1e3
#Z1.Z3/Z2.Z4

if Type=='1' : #L = Z1/Z3
  for Z1 in pignon : 
    for Z3 in couronne :
      if Z1<Z3 :
        L=Z1/Z3
        if Lmin<L and L<Lmax :
          if (Z1+Z3)%Nsat==0: 
            if (Z3-Z1)%2==0 :
              Z2=(Z3-Z1)/2
              if (Zmin<Z2) :
                Zmin=Z2
                print(Z1,Z2,Z3)

if Type=='2' : #L = Z1*Z3/Z2*Z4
  for Z1,Z2,Z3 in pignon:
    for Z4 in couronne :
      if Lmin<(Z1*Z3)/(Z2*Z4)<Lmax :
        if (Z1+Z3)%Nsat==0: 
          if (Z3-Z1)%2==0 :
            Z2=(Z3-Z1)/2
            if Zmin<Z2 :
              print(a)

if Type=='3' : #L = Z1*Z3/Z2*Z4
  for Z1,Z2,Z3,Z4 in range (Zmin,120):
      if Lmin<(Z1*Z3)/(Z2*Z4)<Lmax :
        if (Z1+Z3)%Nsat==0: 
          if (Z3-Z1)%2==0 :
            Z2=(Z3-Z1)/2
            if Zmin<Z2 :
              print(a)

if Type=='4' : #Z1*Z3/Z2*Z4
  for Z1,Z2,Z3,Z4 in range (Zmin,120):
      if Lmin<(Z1*Z3)/(Z2*Z4)<Lmax :
        if (Z1+Z3)%Nsat==0: 
          if (Z3-Z1)%2==0 :
            Z2=(Z3-Z1)/2
            if Zmin<Z2 :
              print(a)

