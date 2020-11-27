# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 12:22:12 2020

@author: HengKang 
Email:kangheng921117@163.com
"""
import os,sys
from shutil import copy
if not os.path.exists("../DW.sh"):
    print "there is no DW.sh file, please check it out!"
    sys.exit()
with open('../DW.sh','r') as p:
    lines=p.readlines()
   # lines=lines.decode("utf-8")
    for line in lines:
        if (line[0:6]=="setenv"):
            value=[str(s) for s in line.split()]
            if(value[1]=="system"):
                system=value[2]
            if(value[1]=="element"):
                element=value[2]
            if(value[1]=="type1"):
                type1=value[2]
            if(value[1]=="type2"):
                type2=value[2]
            if(value[1]=="type3"):
                type3=value[2]
            if(value[1]=="Con_Ini"):
                Con_Ini=value[2]
            if(value[1]=="Potential"):
                Potential=value[2]
            if(value[1]=="T_up"):
                T_up=value[2]
            if(value[1]=="T_low"):
                T_low=value[2]
            if(value[1]=="Cooling_rate"):
                cooling_rate=value[2]
            if(value[1]=="Pressure"):
                Pressure=value[2]
            if(value[1]=="HT_tar_up"):
                HT_tar_up=value[2]
            if(value[1]=="HT_tar_low"):
                HT_tar_low=value[2]
            if(value[1]=="HT_tar_st"):
                HT_tar_st=value[2]
            if(value[1]=="HT_tar_time"):
                HT_tar_time=value[2]
            if(value[1]=="LT_tar_up"):
                LT_tar_up=value[2]
            if(value[1]=="LT_tar_low"):
                LT_tar_low=value[2]
            if(value[1]=="LT_tar_st"):
                LT_tar_st=value[2]
            if(value[1]=="LT_tar_time"):
                LT_tar_time=value[2]
            if(value[1]=="b_block_low"):
                b_block_low=value[2]
            if(value[1]=="b_block_up"):
                b_block_up=value[2]
            if(value[1]=="P_T"):
                P_T=value[2]
            if(value[1]=="timestep"):
                timestep=value[2]
            if(value[1]=="step"):
                step=value[2]
runstep=(int(T_up)-int(T_low))/(float(cooling_rate)*float(timestep))
runstep=int(runstep)
for i in range (int(HT_tar_low),int(HT_tar_up)+int(HT_tar_st),int(HT_tar_st)):
    Hmu=str(i)+"K.restart"    
    copy(Hmu,'dyn')
for i in range (int(LT_tar_low),int(LT_tar_up)+int(LT_tar_st),int(LT_tar_st)):
    Lmu=str(i)+"K.restart"    
    copy(Lmu,'dyn')

