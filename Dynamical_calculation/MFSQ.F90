program mmm
implicit none
integer i,er,j,s,temp1,temp2,temp3,con,m,m1,m2,m3,temp
character*80 f1,f2
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
    read(3,*),temp,ave(j,1),ave(j,2),ave(j,3)
    end do 
c=0.0
do i=1,con
    c(1)=c(1)+ave(i,1)/real(con)
     c(2)=c(2)+ave(i,2)/real(con)
     c(3)=c(3)+ave(i,3)/real(con)
     end do 
    
write(2,"(3(I4))")temp1,temp2,temp3
write(2,*),c(1)
write(2,*),c(2)
write(2,*),c(3)

end 