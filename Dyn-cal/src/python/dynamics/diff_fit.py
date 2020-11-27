# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 12:22:12 2020

@author: HengKang 
Email:kangheng921117@163.com
"""
import numpy as np
import os,sys
#import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
temp1=[]
temp2=[]
tempstep=[]
if os.path.exists('input-DP.txt'):
    print "there is no input-DP.txt file, please confirm you temperature interval in input-DP.txt."
with open("input-DP.txt",'r') as p:
    lines=p.readlines()
    for line in lines:
        value=[int(s) for s in line.split()]   
        temp1.append(value[0])
        temp2.append(value[1])
        tempstep.append(value[2])
print ("###########################################################")
print ("###   if your system is binary system please input 1   ####")
print ("###   if your system is ternary system please input 2  ####")
print ("###########################################################")
print
mm = int(input("Enter your input: "))       
############################################################################       
if(mm==1):
    diffusion1=[]
    diffusion2=[]
    diffusion=[]
    temperature=[]
    for i in range (temp1[0],temp2[0]+tempstep[0],tempstep[0]): 
        temperature.append(i)
        filename=str(i)+"K-msd.txt"
        print ("calculation :",filename)       
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
        fitend=len(X)
        fitup=len(X)-10
        X1=np.array(X[fitup:fitend])
        Y1=np.array(Y[fitup:fitend])
        Z1=np.array(Z[fitup:fitend])
        P1=np.array(P[fitup:fitend])
        def fun(j,a,b):
               return a*j+b
        popt,pcov=curve_fit(fun,X1,Y1)
        popt1,pcov=curve_fit(fun,X1,Z1)
        popt2,pcov=curve_fit(fun,X1,P1)
        d1=popt[0]/6.0
        d2=popt1[0]/6.0
        d3=popt2[0]/6.0
        dd1=d1/100000000.0
        dd2=d2/100000000.0
        dd3=d3/100000000.0
        diffusion1.append(dd1)
        diffusion2.append(dd2)
        diffusion.append(dd3)
    fileout=open("diffusion-co.txt",'w')
    for i in range (0,len(temperature)):
            fileout.write(str(temperature[i])+"\t"+str(diffusion1[i])+"\t"+str(diffusion2[i])+"\t"+str(diffusion[i])+'\n')
if(mm==2):
    diffusion1=[]
    diffusion2=[]
    diffusion3=[]    
    diffusion=[]
    temperature=[]
    for i in range (temp1[0],temp2[0]+tempstep[0],tempstep[0]): 
        temperature.append(i)
        filename=str(i)+"K-msd.txt"
        print ("calculation :",filename)       
        X,Y,Z,V,P = [],[],[],[],[]
        with open(filename, 'r') as f:#1
            line1=f.readline()
            lines = f.readlines()#2
            for line in lines:#3
                value = [float(s) for s in line.split()]#4
                X.append(value[0])#5
                Y.append(value[1])
                Z.append(value[2])
                V.append(value[3])
                P.append(value[4])
        fitend=len(X)
        fitup=len(X)-10
        X1=np.array(X[fitup:fitend])
        Y1=np.array(Y[fitup:fitend])
        Z1=np.array(Z[fitup:fitend])
        V1=np.array(V[fitup:fitend])
        P1=np.array(P[fitup:fitend])
        def fun(j,a,b):
               return a*j+b
        popt,pcov=curve_fit(fun,X1,Y1)
        popt1,pcov=curve_fit(fun,X1,Z1)
        popt2,pcov=curve_fit(fun,X1,V1)        
        popt3,pcov=curve_fit(fun,X1,P1)        
        d1=popt[0]/6.0
        d2=popt1[0]/6.0
        d3=popt2[0]/6.0
        d4=popt3[0]/6.0
        dd1=d1/100000000.0
        dd2=d2/100000000.0
        dd3=d3/100000000.0
        dd4=d4/100000000.0
        diffusion1.append(dd1)
        diffusion2.append(dd2)
        diffusion3.append(dd3)
        diffusion.append(dd4)
    for i in range (0,len(temperature)):
            fileout.write(str(temperature[i])+"\t"+str(diffusion1[i])+"\t"+str(diffusion2[i])+"\t"+str(diffusion3[i])+"\t"+str(diffusion[i])+'\n')

#plt.show()
