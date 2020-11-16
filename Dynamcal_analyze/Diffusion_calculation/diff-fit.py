import numpy as np
#import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math
filename = 'MSD.txt'
X,Y,Z,P = [],[],[],[]
with open(filename, 'r') as f:#1
    line1=f.readline()
    lines = f.readlines()#2
    for line in lines:#3
        value = [float(s) for s in line.split()]#4
        X.append(value[0])#5
        Y.append(value[1])
        Z.append(value[2])
	P.append(value[3])
X1=np.array(X[90:109])
Y1=np.array(Y[90:109])
Z1=np.array(Z[90:109])
P1=np.array(P[90:109])
def fun(j,a,b):
       return a*j+b
popt,pcov=curve_fit(fun,X1,Y1)
popt1,pcov=curve_fit(fun,X1,Z1)
popt2,pcov=curve_fit(fun,X1,P1)
#p=np.arange(200,1000)
#plt.scatter(X,Y,c="r")
#plt.scatter(X,Z,c="y")
#plt.scatter(X,P,c="b")
#plt.plot(p,fun(p,*popt),"r")
#plt.plot(p,fun(p,*popt1),"y")
#plt.plot(p,fun(p,*popt2),"b")
d1=popt[0]/6.0
d2=popt1[0]/6.0
d3=popt2[0]/6.0
dd1=d1/100000000.0
dd2=d2/100000000.0
dd3=d3/100000000.0
fileout=open('DIFFUSION.txt','w')
fileout.write(str(dd1)+'\n')
fileout.write(str(dd2)+'\n')
fileout.write(str(dd3))

#plt.show()
