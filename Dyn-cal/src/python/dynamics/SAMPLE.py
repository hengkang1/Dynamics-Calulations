# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 12:22:12 2020

@author: HengKang 
Email:kangheng921117@163.com
"""
import os,sys
from shutil import copy
if not os.path.exists("DW.sh"):
    print "there is no DW.sh file, please check it out!"
    sys.exit()
with open('DW.sh','r') as p:
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
            if(value[1]=='mpi_commd'):
		mpi_commd=value[2]
	    if(value[1]=='LAMMPS_commd'):
                LAMMPS_commd=value[2]
	    if(value[1]=='mpi_np'):
                mpi_np=value[2]		
op=open("ff",'w')
op.write(str(system)+'\n')
op.write(str(mpi_commd)+'\n')
op.write(str(LAMMPS_commd)+'\n')
op.write(str(mpi_np)+'\n')
runstep=(int(T_up)-int(T_low))/(float(cooling_rate)*float(timestep))
runstep=int(runstep)
if os.path.exists(system):
    os.system("rm -r "+system)    
os.mkdir(system)
copy(Con_Ini,system)
copy(Potential,system)
runt=int(1.0/(float(cooling_rate)*float(timestep)))
runt10=runt*10
f=open(system+'/in-1.melt','w')
f.write("units           metal"+'\n')
f.write("boundary        p p p"+'\n')
f.write('atom_style      atomic'+'\n')
f.write('read_data       '+Con_Ini+'\n') 
f.write('')
f.write('pair_style      '+P_T+'\n')
if(element=='3'):
    f.write('pair_coeff   * *  ' +Potential + '  '+type1 +'  '+ type2+ '  '+type3+'\n')
if(element=='2'):
    f.write('pair_coeff   * *  ' +Potential + '  '+type1 +'  '+ type2+'\n')
f.write(''+'\n')
f.write('neighbor        2.0 bin'+'\n')
f.write('neigh_modify    delay 10'+'\n')
f.write('timestep        '+timestep+'\n')
f.write('thermo_style    custom step temp pe ke enthalpy vol lx ly lz'+'\n')
f.write('thermo          10000'+'\n')
f.write('variable         S equal step'+'\n')
f.write('variable         T equal temp'+'\n')
f.write('variable         Ep equal pe'+'\n')
f.write('variable         H equal enthalpy'+'\n')
f.write('variable         V equal vol'+'\n')
f.write('fix        1 all npt temp '+T_up+" "+T_up+' 0.1 iso '+Pressure+' '+Pressure+' 1.0 drag 0.2'+'\n')
f.write('fix          2 all print 1000 "${S} ${T} ${Ep} ${H} ${V}" file thermo-1.txt'+'\n')
f.write('run              1000000'+'\n')
f.write('unfix            1'+'\n')
f.write('unfix            2'+'\n')
f.write('reset_timestep   0'+'\n')
f.write('dump             1 all custom '+str(runt10)+' det.lammpstrj id type x y z '+'\n')
f.write('fix              1 all npt temp '+T_up+" "+T_low+' 0.1 iso '+Pressure+' '+Pressure+' 1.0 drag 0.2'+'\n')
f.write('fix          2 all print 1000 "${S} ${T} ${Ep} ${H} ${V}" file thermo-2.txt'+'\n')
f.write('run              '+str(runstep)+'\n')
##########################################################################################
a=(int(HT_tar_up)-int(HT_tar_low))/int(HT_tar_st)
a=a+1
b=(int(LT_tar_up)-int(LT_tar_low))/int(LT_tar_st)
b=b+1
Hf=(int(T_up)-int(HT_tar_up))/(float(cooling_rate)*float(timestep))
Hf=int(Hf)
Lf=(int(T_up)-int(LT_tar_up))/(float(cooling_rate)*float(timestep))
Lf=int(Lf)
f=open(system+'/in-2.melt','w')
f.write("####equilibrium in high temperature"+'\n')
f.write(""+'\n')
f.write('label           loop1'+'\n')
f.write('variable        a loop '+str(a)+'\n')
f.write('variable        T0 equal "'+HT_tar_up+'-(v_a-1)*'+HT_tar_st+'"'+'\n')
f.write('variable        Ns equal "'+str(Hf)+'+(v_a-1)*'+HT_tar_st+'*'+str(runt)+'"'+'\n')
f.write(""+'\n')
f.write('units           metal'+'\n')
f.write('boundary        p p p'+'\n')
f.write('atom_style      atomic'+'\n')
f.write('read_data       in.data '+'\n')
f.write(""+'\n')
f.write('read_dump       det.lammpstrj ${Ns} x y z'+'\n')
f.write('pair_style      eam/alloy'+'\n')
f.write('pair_coeff      * *  ZrCu.lammps.eam Zr Cu'+'\n')
f.write('neighbor        2.0 bin'+'\n')
f.write('neigh_modify    delay 10'+'\n')
f.write('timestep        0.001'+'\n')
f.write(""+'\n')
f.write('reset_timestep   0'+'\n')
f.write('thermo_style    custom step temp pe ke enthalpy vol lx ly lz'+'\n')
f.write('thermo          10000'+'\n')
f.write('variable         S equal step'+'\n')
f.write('variable         T equal temp'+'\n')
f.write('variable         Ep equal pe'+'\n')
f.write('variable         H equal enthalpy'+'\n')
f.write('variable         V equal vol'+'\n')
f.write(""+'\n')
f.write('fix   1 all npt temp ${T0} ${T0} 0.1 iso 0 0 1.0 drag 0.2'+'\n')
f.write('fix   2 all print 1000 "${S} ${T} ${Ep} ${H} ${V}" file thermoeq-${T0}K.txt'+'\n')
f.write('run              '+str(int(float(HT_tar_time)/float(timestep)))+'\n')
f.write('unfix            1'+'\n')
f.write('unfix            2'+'\n')
f.write('write_restart    ${T0}K.restart'+'\n')
f.write('clear'+'\n')
f.write('next  a'+'\n')
f.write('jump              in-2.melt loop1'+'\n')
f.write(""+'\n')
f.write("###equilibrium in low temperature"+'\n')
f.write(""+'\n')
f.write('label           loop2'+'\n')
f.write('variable        b loop '+str(b)+'\n')
f.write('variable        T0 equal "'+LT_tar_up+'-(v_b-1)*'+LT_tar_st+'"'+'\n')
f.write('variable        Ns equal "'+str(Lf)+'+(v_b-1)*'+LT_tar_st+'*'+str(runt)+'"'+'\n')
f.write(""+'\n')
f.write('units           metal'+'\n')
f.write('boundary        p p p'+'\n')
f.write('atom_style      atomic'+'\n')
f.write('read_data       in.data '+'\n')
f.write('read_dump       det.lammpstrj ${Ns} x y z'+'\n')
f.write(""+'\n')
f.write('pair_style      eam/alloy'+'\n')
f.write('pair_coeff      * *  ZrCu.lammps.eam Zr Cu'+'\n')
f.write('neighbor        2.0 bin'+'\n')
f.write('neigh_modify    delay 10'+'\n')
f.write('timestep        0.001'+'\n')
f.write('reset_timestep   0'+'\n')
f.write('thermo_style    custom step temp pe ke enthalpy vol lx ly lz'+'\n')
f.write('thermo          10000'+'\n')
f.write(""+'\n')
f.write('variable         S equal step'+'\n')
f.write('variable         T equal temp'+'\n')
f.write('variable         Ep equal pe'+'\n')
f.write('variable         H equal enthalpy'+'\n')
f.write('variable         V equal vol'+'\n')
f.write(""+'\n')
f.write('fix   1 all npt temp ${T0} ${T0} 0.1 iso 0 0 1.0 drag 0.2'+'\n')
f.write('fix   2 all print 1000 "${S} ${T} ${Ep} ${H} ${V}" file thermoeq-${T0}K.txt'+'\n')
f.write('run              '+str(int(float(LT_tar_time)/float(timestep)))+'\n')
f.write('unfix            1'+'\n')
f.write('unfix            2'+'\n')
f.write('write_restart    ${T0}K.restart'+'\n')
f.write('clear'+'\n')
f.write('next  b'+'\n')
f.write('jump              in-2.melt loop2'+'\n')
#####################################################
os.mkdir(system+'/dyn')
copy(Potential,system+'/dyn')
copy("dd.txt",system+'/dyn')
copy("dp.txt",system+'/dyn')
f=open(system+'/dyn/in-dy.melt','w')
f.write("###dynamical configuration at high temperature"+'\n')
f.write(" "+'\n')
f.write("variable       Tb  equal "+HT_tar_up+'\n')
f.write("variable       Te  equal "+HT_tar_low+'\n')
f.write("variable       dT  equal "+HT_tar_st+'\n')
f.write("variable       ss equal 1000000"+'\n')
f.write("variable       st equal 'v_ss+990000'"+'\n')
f.write("variable       sa equal 'v_st/1000'"+'\n')
f.write("variable       nT  equal '(v_Tb-v_Te)/v_dT+1'"+'\n')
f.write("label          loop1"+'\n')
f.write("variable       a loop ${nT}"+'\n')
f.write("variable       temp0 equal 'v_Tb-(v_a-1)*v_dT'"+'\n')
f.write("units           metal"+'\n')
f.write("boundary        p p p"+'\n')
f.write(""+'\n')
f.write("atom_style      atomic"+'\n')
f.write("read_restart    ${temp0}K.restart "+'\n')
f.write("reset_timestep  0"+'\n')
f.write("pair_style      eam/alloy"+'\n')
f.write("pair_coeff      * *  ZrCu.lammps.eam Zr Cu"+'\n')
f.write("neighbor        2.0 bin"+'\n')
f.write("neigh_modify    delay 10"+'\n')
f.write("timestep        0.001"+'\n')
f.write("thermo_style    custom step temp pe ke enthalpy vol lx ly lz"+'\n')
f.write("thermo          10000"+'\n')
f.write("variable        n file dd.txt"+'\n')
f.write("variable        f equal next(n)"+'\n')
f.write("variable        m file dp.txt"+'\n')
f.write("variable        s equal next(m)"+'\n')
f.write("dump             2 all custom 10000 ${temp0}K-cfg.lammpstrj id type x y z"+'\n')
f.write("dump             3 all custom 1 ${temp0}K-dis.lammpstrj id type xu yu zu"+'\n')
f.write("dump_modify      2 every v_f first yes"+'\n')
f.write("dump_modify      3 every v_s first yes"+'\n')
f.write("fix              1 all npt temp ${temp0} ${temp0} 0.1 iso "+Pressure+" "+Pressure+' 0.75'+'\n')
f.write("run              ${st}"+'\n')
f.write("unfix            1"+'\n')
f.write("undump           2"+'\n')
f.write("undump           3"+'\n')
f.write("variable        n delete"+'\n')
f.write("variable        f delete"+'\n')
f.write("variable        m delete"+'\n')
f.write("variable        s delete"+'\n')
f.write("clear"+'\n')
f.write("next        a"+'\n')
f.write("jump        in-dy.melt   loop1"+'\n')
f.write("##dynamical configuration at low temperature"+'\n')
f.write(" "+'\n')
f.write("variable       Tb  equal "+LT_tar_up+'\n')
f.write("variable       Te  equal "+LT_tar_low+'\n')
f.write("variable       dT  equal "+LT_tar_st+'\n')
f.write("variable       ss equal 10000000"+'\n')
f.write("variable       st equal 'v_ss+990000'"+'\n')
f.write("variable       sa equal 'v_st/1000'"+'\n')
f.write("variable       nT  equal '(v_Tb-v_Te)/v_dT+1'"+'\n')
f.write("label          loop2"+'\n')
f.write("variable       b loop ${nT}"+'\n')
f.write("variable       temp0 equal 'v_Tb-(v_b-1)*v_dT'"+'\n')
f.write("units           metal"+'\n')
f.write("boundary        p p p"+'\n')
f.write(""+'\n')
f.write("atom_style      atomic"+'\n')
f.write("read_restart    ${temp0}K.restart "+'\n')
f.write("reset_timestep  0"+'\n')
f.write("pair_style      eam/alloy"+'\n')
f.write("pair_coeff      * *  ZrCu.lammps.eam Zr Cu"+'\n')
f.write("neighbor        2.0 bin"+'\n')
f.write("neigh_modify    delay 10"+'\n')
f.write("timestep        0.001"+'\n')
f.write("thermo_style    custom step temp pe ke enthalpy vol lx ly lz"+'\n')
f.write("thermo          10000"+'\n')
f.write("variable        n file dd.txt"+'\n')
f.write("variable        f equal next(n)"+'\n')
f.write("variable        m file dp.txt"+'\n')
f.write("variable        s equal next(m)"+'\n')
f.write("dump             2 all custom 10000 ${temp0}K-cfg.lammpstrj id type x y z"+'\n')
f.write("dump             3 all custom 1 ${temp0}K-dis.lammpstrj id type xu yu zu"+'\n')
f.write("dump_modify      2 every v_f first yes"+'\n')
f.write("dump_modify      3 every v_s first yes"+'\n')
f.write("fix              1 all npt temp ${temp0} ${temp0} 0.1 iso "+Pressure+" "+Pressure+' 0.75'+'\n')
f.write("run              ${st}"+'\n')
f.write("unfix            1"+'\n')
f.write("undump           2"+'\n')
f.write("undump           3"+'\n')
f.write("variable        n delete"+'\n')
f.write("variable        f delete"+'\n')
f.write("variable        m delete"+'\n')
f.write("variable        s delete"+'\n')
f.write("clear"+'\n')
f.write("next        b"+'\n')
f.write("jump        in-dy.melt   loop2"+'\n')





































 










































































