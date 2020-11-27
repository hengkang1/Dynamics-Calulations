program sqmax
implicit none
character*80 i
read(*,*),i
if(trim(adjustl(i))=="1")call binary
if(trim(adjustl(i))=="2")call ternary
end
!####
subroutine binary
implicit none
integer i,er,j,s,temp1,temp2,temp3,con,m,temp
character*80 f1
real a(1000000),b1(1000000),b2(1000000),b3(1000000),b4(1000000),c(3) 
real,allocatable:: ave(:,:)
open(unit=1,file="input-DP.txt")
open(unit=3,file="maxsq.txt")
read(1,*),temp1,temp2,temp3
con=(temp2-temp1)/temp3+1
close(1)
allocate(ave(con,3))
open(unit=2,file="input-DP.txt")
s=0
do j=temp1,temp2,temp3
s=s+1
write(f1,"(I4)")j
m=1
open(unit=1,file=trim(adjustl(f1))//"K-sq.txt")
do while(.true.)
read(1,*,iostat=er),a(m),b1(m),b2(m),b3(m),b4(m)
m=m+1
if(er/=0)exit
end do 
close(1)
write(3,"((I4),3(f12.6))")j,a(maxLoc(b1)),a(maxLoc(b3)),a(maxLoc(b4))
end do 
close(3)
open(unit=3,file="maxsq.txt")
do j=1,con
    read(3,"((I5),3(F12.6))"),temp,ave(j,1),ave(j,2),ave(j,3)
    end do 
c=0.0
do i=1,con
     c(1)=c(1)+ave(i,1)/real(con)
     c(2)=c(2)+ave(i,2)/real(con)
     c(3)=c(3)+ave(i,3)/real(con)
     end do     
write(2,"(3(I6))")temp1,temp2,temp3
write(2,*),c(1)
write(2,*),c(2)
write(2,*),c(3)
end 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!
subroutine ternary
implicit none
integer i,er,j,s,temp1,temp2,temp3,con,m,temp
character*80 f1
real a(1000000),b1(1000000),b2(1000000),b3(1000000),b4(1000000),c(4) 
real b5(1000000),b6(1000000),b7(1000000)
real,allocatable:: ave(:,:)
open(unit=1,file="input-DP.txt")
open(unit=3,file="maxsq.txt")
read(1,*),temp1,temp2,temp3
con=(temp2-temp1)/temp3+1
close(1)
allocate(ave(con,4))
open(unit=2,file="input-DP.txt")
s=0
do j=temp1,temp2,temp3
s=s+1
write(f1,"(I4)")j
m=1
open(unit=1,file=trim(adjustl(f1))//"K-sq.txt")
do while(.true.)
read(1,*,iostat=er),a(m),b1(m),b2(m),b3(m),b4(m),b5(m),b6(m),b7(m)
m=m+1
if(er/=0)exit
end do 
close(1)
write(3,"((I4),3(f12.6))")j,a(maxLoc(b1)),a(maxLoc(b4)),a(maxLoc(b6)),a(maxLoc(b7))
end do 
close(3)
open(unit=3,file="maxsq.txt")
do j=1,con
    read(3,*),temp,ave(j,1),ave(j,2),ave(j,3),ave(j,4)
    end do 
c=0.0
do i=1,con
    c(1)=c(1)+ave(i,1)/real(con)
     c(2)=c(2)+ave(i,2)/real(con)
     c(3)=c(3)+ave(i,3)/real(con)
     c(4)=c(4)+ave(i,3)/real(con)
     end do 
write(2,"(3(I4))")temp1,temp2,temp3
write(2,*),c(1)
write(2,*),c(2)
write(2,*),c(3)
write(2,*),c(4)
end 
