program diff
integer i,temp,er,temp1,temp2,temp3
real dis,a,b,c,d1,d2,d3 
character*80 f1,f2,f3
open(unit=10,file="input-DP.txt")
read(10,*),temp1,temp2,temp3
open(unit=4,file="diff-data.txt")
do i=temp1,temp2,temp3
write(f1,"(I4)"),i
f2=trim(adjustl(f1))//"K-msd.txt"
print*,"calculate:  ",f2
open(unit=1,file=f2)
open(unit=2,file="MSD.txt")
do while(.true.)
read(1,*,iostat=er),dis,a,b,c
if(a==0.or.b==0.or.c==0)cycle
write(2,"(4(f20.12))"),dis,a,b,c
if(er/=0)exit
end do 
close(1)
close(2)
call system("diff-fit.exe")
open(unit=3,file="DIFFUSION.txt")
read(3,*),d1
read(3,*),d2
read(3,*),d3
write(4,"(I4,3(E20.12))"),i,d1,d2,d3
close(3)
end do 
end
