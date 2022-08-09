import numpy as np

#equation de la forme Δε = A x Nf^-α

# m = ordonnée à l'origine 
m = 0.40

#Rentrer point
XA = 313000
YA = 600

#Rentrer point 
LOGX = 4600000
LOGY = 435

α=-(-np.log(YA)+np.log(LOGY))/(+np.log(LOGX)-np.log(XA))

print('Δε = %0.6f x Nf^%0.6f'%(m,α))