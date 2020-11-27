program runsimulation
implicit none
character*400 f1,f2,f3,f4,f5,f6,f7,ff,f8,ff1,f9,f10
character*400 path1,path2,fp,fj,mpi,lamm,np
open(unit=3,file="ff")
read(3,*),fp
read(3,*),mpi
read(3,*),lamm
read(3,*),np
call system("rm ff")
f3="cd "//trim(adjustl(fp))//" && "
f4=trim(adjustl(mpi))//" -np "//trim(adjustl(np))//" "//trim(adjustl(lamm))//" <in-1.melt && "
f5=trim(adjustl(mpi))//" -np "//trim(adjustl(np))//" "//trim(adjustl(lamm))//" <in-2.melt && "
f6="Dyrun2 &&"
f7="cd dyn && "
f8=trim(adjustl(mpi))//" -np "//trim(adjustl(np))//" "//trim(adjustl(lamm))//" <in-dy.melt"
f9=trim(adjustl(f3))//trim(adjustl(f4))//trim(adjustl(f5))//trim(adjustl(f6))//trim(adjustl(f7))//trim(adjustl(f8))
call system(f9)
end

