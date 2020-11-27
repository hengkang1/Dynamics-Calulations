program mm
implicit none
integer i
character*80 f1,f2
print*, "###########################################################"
print*, "###   if your system is binary system please input 1   ####"
print*, "###   if your system is ternary system please input 2  ####"
print*, "###########################################################"
print*,
10 print*,"please input your number:"
read(*,*),i
if(i.lt.1.and.i.gt.2)then
    print*,"your number is wrong!!"
    go to 10
end if
write(f1,"(I3)")i
f2="pdf && echo "//trim(adjustl(f1))//"|MFSQ && pdt"
call system(f2)
end 
