from sqlite3 import DataError, DatabaseError
import numpy as np 


class calculator:
    def Calcul(self, d,D,R,e):
        A=d*D 
        B=R*e
        C=[A,B]
        return C

#print('V1 = %0.6f mm\nV2 = %0.6f mm\nV3 = %0.6f mm\n'%(x1,x2,x3))