# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 21:30:01 2020

@author: Administrator
"""
from scipy import interpolate
import matplotlib.pyplot as plt
import math
import pylab as pl

temp1=[]
temp2=[]
tempstep=[]
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
if(mm==1):
####################binary system
    relaxationtime1=[]
    relaxationtime2=[]
    relaxationtimet=[]
    temperature=[]
    ret=math.exp(-1)
    for i in range (temp1[0],temp2[0]+tempstep[0],tempstep[0]): 
        temperature.append(i)
        filename=str(i)+"K-isf.txt"
        print ("calculation :",filename)
        time=[]
        isf1=[]
        isf2=[]
        isft=[]
        inter=[]
        xdata1=[]
        xdatanew1=[]
        ydatanew1=[]
        ydata1=[]
        xdata2=[]
        xdatanew2=[]
        ydatanew2=[]
        ydata2=[]
        xdatat=[]
        xdatanewt=[]
        ydatanewt=[]
        ydatat=[]
        testx=[]
        testy=[]
        cc=[]
        with open(filename,'r') as f :
            lines=f.readlines()
            for line in lines:
                value=[float(s) for s in line.split()]
                if(value[1]>0 ):
                    time.append(value[0])
                    isf1.append(value[1])
                    isf2.append(value[2])
                    isft.append(value[3])
        ao=len(time)
        ############################
        rec1=ao
        rec2=ao
        rect=ao
        for i in range (0,ao-1):
            if((isf1[i]-ret)>0 and (isf1[i+1]-ret)<0):
                rec1=i
            if((isf2[i]-ret)>0 and (isf2[i+1]-ret)<0):
                rec2=i
            if((isft[i]-ret)>0 and (isft[i+1]-ret)<0):
                rect=i
       
        #############################################################
        #start interpolate
        #########################################################
        if(rec1+2<=(ao-1)):    
            for i in range (rec1-8,rec1+2):
                a=time[i]
                xdata1.append(a)
                b=isf1[i]
                ydata1.append(b)
            for i in range (0,999):
                m=xdata1[0]+i*(xdata1[len(xdata1)-1]-xdata1[0])/1000    
                xdatanew1.append(m)
            f=interpolate.interp1d(xdata1,ydata1,kind='cubic')
            ydatanew1=f(xdatanew1)
            for i in range (0,998):
                if((ydatanew1[i]-ret)>0 and (ydatanew1[i+1]-ret)<=0):
                   a=i
            relaxationtime1.append(xdatanew1[a]) 
        else:
            relaxationtime1.append("NAN")
            print ("element 1 need a relxation for a long time in",filename)
        #################################################################
        if(rec2+2<=(ao-1)):     
            for i in range (rec2-8,rec2+2):
                a=time[i]
                xdata2.append(a)
                b=isf2[i]
                ydata2.append(b)
            for i in range (0,999):
                m=xdata2[0]+i*(xdata2[len(xdata2)-1]-xdata2[0])/1000
                xdatanew2.append(m)
            f=interpolate.interp1d(xdata2,ydata2,kind='cubic')
            ydatanew2=f(xdatanew2)
            for i in range (0,998):
                if((ydatanew2[i]-ret)>0 and (ydatanew2[i+1]-ret)<=0):
                    b=i
            relaxationtime2.append(xdatanew2[b])
        else:
            relaxationtime2.append("NAN")
            print ("element 2 need a relxation for a long time in",filename)
        #####################################################################
        if(rect+2<=(ao-1)):
            for i in range (rect-8,rect+2):
                a=time[i]
                xdatat.append(a)
                b=isft[i]
                ydatat.append(b)
            for i in range (0,999):
                m=xdatat[0]+i*(xdatat[len(xdatat)-1]-xdatat[0])/1000
                xdatanewt.append(m)
            f=interpolate.interp1d(xdatat,ydatat,kind='cubic')
            ydatanewt=f(xdatanewt)
            for i in range (0,998):
                if((ydatanewt[i]-ret)>0 and (ydatanewt[i+1]-ret)<=0):
                    d=i
            relaxationtimet.append(xdatanewt[d])
        else:
            relaxationtimet.append("NAN") 
            print ("system need a relxation for a long time in",filename)
        #######################################################################
            
    ###########################################
    fileout=open("relaxation_time.txt",'w')
    for i in range (0,len(temperature)):
            fileout.write(str(temperature[i])+"\t"+str(relaxationtime1[i])+"\t"+str(relaxationtime2[i])+"\t"+str(relaxationtimet[i])+'\n')
if (mm==2):
######################################tenary system    
    relaxationtime1=[]
    relaxationtime2=[]
    relaxationtime3=[]
    relaxationtimet=[]
    temperature=[]
    ret=math.exp(-1)
    for i in range (temp1[0],temp2[0]+tempstep[0],tempstep[0]): 
        temperature.append(i)
        filename=str(i)+"K-isf.txt"
        print ("calculation :",filename)
        time=[]
        isf1=[]
        isf2=[]
        isf3=[]
        isft=[]
        inter=[]
        xdata1=[]
        xdatanew1=[]
        ydatanew1=[]
        ydata1=[]
        xdata2=[]
        xdatanew2=[]
        ydatanew2=[]
        ydata2=[]
        xdata3=[]
        xdatanew3=[]
        ydatanew3=[]
        ydata3=[]
        xdatat=[]
        xdatanewt=[]
        ydatanewt=[]
        ydatat=[]
        testx=[]
        testy=[]
        cc=[]
        with open(filename,'r') as f :
            lines=f.readlines()
            for line in lines:
                value=[float(s) for s in line.split()]
                if(value[1]>0 ):
                    time.append(value[0])
                    isf1.append(value[1])
                    isf2.append(value[2])
                    isf3.append(value[3])
                    isft.append(value[4])
        ao=len(time)
        ############################
        rec1=ao
        rec2=ao
        rec3=ao
        rect=ao
        for i in range (0,ao-1):
            if((isf1[i]-ret)>0 and (isf1[i+1]-ret)<0):
                rec1=i
            if((isf2[i]-ret)>0 and (isf2[i+1]-ret)<0):
                rec2=i
            if((isf3[i]-ret)>0 and (isf3[i+1]-ret)<0):
                rec3=i
            if((isft[i]-ret)>0 and (isft[i+1]-ret)<0):
                rect=i
       
        #############################################################
        #start interpolate
        #########################################################
        if(rec1+2<=(ao-1)):    
            for i in range (rec1-8,rec1+2):
                a=time[i]
                xdata1.append(a)
                b=isf1[i]
                ydata1.append(b)
            for i in range (0,999):
                m=xdata1[0]+i*(xdata1[len(xdata1)-1]-xdata1[0])/1000    
                xdatanew1.append(m)
            f=interpolate.interp1d(xdata1,ydata1,kind='cubic')
            ydatanew1=f(xdatanew1)
            for i in range (0,998):
                if((ydatanew1[i]-ret)>0 and (ydatanew1[i+1]-ret)<=0):
                   a=i
            relaxationtime1.append(xdatanew1[a]) 
        else:
            relaxationtime1.append("NAN")
            print ("element 1 need a relxation for a long time in",filename)
        #################################################################
        if(rec2+2<=(ao-1)):     
            for i in range (rec2-8,rec2+2):
                a=time[i]
                xdata2.append(a)
                b=isf2[i]
                ydata2.append(b)
            for i in range (0,999):
                m=xdata2[0]+i*(xdata2[len(xdata2)-1]-xdata2[0])/1000
                xdatanew2.append(m)
            f=interpolate.interp1d(xdata2,ydata2,kind='cubic')
            ydatanew2=f(xdatanew2)
            for i in range (0,998):
                if((ydatanew2[i]-ret)>0 and (ydatanew2[i+1]-ret)<=0):
                    b=i
            relaxationtime2.append(xdatanew2[b])
        else:
            relaxationtime2.append("NAN")
            print ("element 2 need a relxation for a long time in",filename)
        #####################################################################
        if(rec3+2<=(ao-1)):    
            for i in range (rec3-8,rec3+2):
                a=time[i]
                xdata3.append(a)
                b=isf3[i]
                ydata3.append(b)
            for i in range (0,999):
                m=xdata3[0]+i*(xdata3[len(xdata3)-1]-xdata3[0])/1000    
                xdatanew3.append(m)
            f=interpolate.interp1d(xdata3,ydata3,kind='cubic')
            ydatanew3=f(xdatanew3)
            for i in range (0,998):
                if((ydatanew3[i]-ret)>0 and (ydatanew3[i+1]-ret)<=0):
                   a=i
            relaxationtime3.append(xdatanew3[a]) 
        else:
            relaxationtime3.append("NAN")
            print ("element 3 need a relxation for a long time in",filename)   
        ####################################################################
        if(rect+2<=(ao-1)):
            for i in range (rect-8,rect+2):
                a=time[i]
                xdatat.append(a)
                b=isft[i]
                ydatat.append(b)
            for i in range (0,999):
                m=xdatat[0]+i*(xdatat[len(xdatat)-1]-xdatat[0])/1000
                xdatanewt.append(m)
            f=interpolate.interp1d(xdatat,ydatat,kind='cubic')
            ydatanewt=f(xdatanewt)
            for i in range (0,998):
                if((ydatanewt[i]-ret)>0 and (ydatanewt[i+1]-ret)<=0):
                    d=i
            relaxationtimet.append(xdatanewt[d])
        else:
            relaxationtimet.append("NAN") 
            print ("system need a relxation for a long time in",filename)
        #######################################################################
    fileout=open("relaxation_time.txt",'w')
    for i in range (0,len(temperature)):
            fileout.write(str(temperature[i])+"\t"+str(relaxationtime1[i])+"\t"+str(relaxationtime2[i])+"\t"+str(relaxationtime3[i])+"\t"+str(relaxationtimet[i])+'\n')    
  
    
    
    
    
    
    
    
    
    
    
    
    
        
