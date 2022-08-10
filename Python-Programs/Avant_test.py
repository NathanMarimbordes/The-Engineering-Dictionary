
import matplotlib.pyplot as plt
from HospitalApi import test

d = [test.d for test in test]
D = [test.D for test in test]
a = [test.a for test in test]
z = [test.z for test in test]


import numpy as np 

# TEST PREMIERE UTILISATION DE PYTHON DANS DU C#

#On donne au début 3 variables simples.
#Calcul rapide évidemment
S1 =d+D
S2 =z
S3 =a

print('S1 = %0.6f mm\n S2 = %0.6f mm\n S3 = %0.6f mm\n'%(S1,S2,S3))