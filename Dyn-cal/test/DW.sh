#_________________________________sample preparation
setenv system  ZrCu #please named your simulation system
setenv element 2 #confirm the number of elements in your system 
setenv type1   Zr #label elements 
setenv type2   Cu
#setenv type3   Al
setenv Con_Ini in.data #your initial configuration file name 
setenv P_T eam/alloy #your potential type
setenv Potential ZrCu.lammps.eam #potential file name
setenv T_up 2000    #start temperature in cooling process
setenv T_low 300    #end temperature in cooling process
setenv Pressure 0    #pressure of simulation (this unit is Bar)
setenv timestep 0.001  #timestep of simulation (this unit is ps)
setenv Cooling_rate 10 #cooling rate (this unit is K/ps)
#_________________________________equilibrium
###########Below, temperature interval calculte dynamcis for 1000ps 
setenv HT_tar_up 800   #start temperature
setenv HT_tar_low 700  #end temperature
setenv HT_tar_st  100   #interval of temperature
setenv HT_tar_time 1000 #time of equilibrium (This unit is ps)
############Below, temperature interval calculate dynamics for 10000ps
setenv LT_tar_up  600  #start temperature
setenv LT_tar_low 500   #end temperature
setenv LT_tar_st  100   #interval of termperature
setenv LT_tar_time 1000 #time of equilibrium (This unit is ps)
#_________________________________mpirun calculation
setenv mpi_commd mpirun # your system mpi command
setenv LAMMPS_commd lmp_mpi #your LAMMPS  executive program
setenv mpi_np 12 #applying for CPU cores

