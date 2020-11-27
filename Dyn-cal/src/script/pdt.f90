program DynamicProperty
implicit none
integer nr,nt,ne,bj(100000000),i,i0,j,typ(10000),id,step,n,nd,bh1(100000000),bh2(100000),bh
integer ntype,ntyp(3),er,natom,ntt,Tb,Te,Ts
real emax,de,zb(10000,3),rzb(100,10000,3),dx,dy,dz,dis,qm,qmax(4),qq
real(8) msd(100000),isf(100000),ngf(100000),pmsd(3,100000),pisf(3,100000),pngf(3,100000),is,ms,ng,pms(3),pis(3),png(3)
logical alive
character*8 f1
nr=100    !the number of referred cfgs
nt=10000  !The times between referred cfgs
emax=8.0  !the max timestep is 10**(emax)
de=0.05   
ne=int(emax/de)
inquire(file='input-DP.txt',exist=alive)
if(.not.alive)then
   print*,'No input file with the vetors for ISF:input-DP.txt.'
   stop
endif
open(unit=1,file='input-DP.txt')
read(1,*)Te,Tb,Ts
ntt=0
do while(.true.)
   read(1,*,iostat=er)qq
   if(er/=0)exit
   ntt=ntt+1
   qmax(ntt)=qq
enddo
close(1)
qm=qmax(ntt)
ntt=ntt-1
print*,ntt
bj=0
do i=0,ne
    bj(int(10.0**(real(i)*de)))=1
enddo

nd=0
do i=1,100000000
    if(bj(i)==1)then
      nd=nd+1
      bh1(i)=nd
      bh2(nd)=i
    endif
enddo

do i0=Te,Tb,Ts
    write(f1,'(I5)')i0
    inquire(file=trim(adjustl(f1))//'K-dis.lammpstrj',exist=alive)
    if(.not.alive)cycle
    msd=0.0
    isf=0.0
    pmsd=0.0
    pisf=0.0
    ngf=0.0
    pngf=0.0
    print*,'The temperature is ',f1
    open(unit=1,file=trim(adjustl(f1))//'K-dis.lammpstrj')
    do while(.true.)
       read(1,*,iostat=er)
       if(er/=0)exit
       read(1,*)step
       read(1,*)
       read(1,*)natom
       do i=1,5
          read(1,*)
       enddo
       ntyp=0
       ntype=0
       do i=1,natom
          read(1,*)id,typ(id),(zb(id,j),j=1,3)
          ntyp(typ(id))=ntyp(typ(id))+1
          if(typ(id)>ntype)ntype=typ(id)
       enddo
       if(ntype/=ntt)then
          print*,'wrong numbers of vetors for ISFs, please check'
          stop
       endif
       !_______________________________________________________________________
       if(step<nr*nt.and.mod(step,nt)==0)then
          n=step/nt+1
          do i=1,natom
               rzb(n,i,1)=zb(i,1)                           !标记原点
               rzb(n,i,2)=zb(i,2)
               rzb(n,i,3)=zb(i,3)
          enddo
       endif
       !____________________________________________________________________________
       do i=1,nr
         if(step-(i-1)*nt<0)exit
         if(bj(step-(i-1)*nt)==0)cycle
         ms=0.0
         pms=0.0
         is=0.0
         pis=0.0
         ng=0.0
         png=0.0
         n=step-(i-1)*nt
         do j=1,natom
              dx=zb(j,1)-rzb(i,j,1)
              dy=zb(j,2)-rzb(i,j,2)
              dz=zb(j,3)-rzb(i,j,3)
              dis=dx*dx+dy*dy+dz*dz
              ms=ms+dis/real(natom)
              is=is+(cos(qm*dx)+cos(qm*dy)+cos(qm*dz))/3.0/real(natom)
              ng=ng+dis**2/real(natom)
              bh=typ(j)
              qq=qmax(bh)
              pms(bh)=pms(bh)+dis/real(ntyp(bh))
              pis(bh)=pis(bh)+(cos(qq*dx)+cos(qq*dy)+cos(qq*dz))/3.0/real(ntyp(bh))
              png(bh)=png(bh)+dis**2/real(ntyp(bh))
         enddo 
         ng=0.6*ng/ms/ms-1.0
         do j=1,ntype
             png(j)=png(j)*0.6/pms(j)/pms(j)-1.0
         enddo
         msd(bh1(n))=msd(bh1(n))+ms/100.0
         isf(bh1(n))=isf(bh1(n))+is/100.0
         ngf(bh1(n))=ngf(bh1(n))+ng/100.0
         do j=1,ntype
             pmsd(j,bh1(n))=pmsd(j,bh1(n))+pms(j)/100.0
             pisf(j,bh1(n))=pisf(j,bh1(n))+pis(j)/100.0
             pngf(j,bh1(n))=pngf(j,bh1(n))+png(j)/100.0
         enddo
      enddo
    enddo
    close(1)
     n=bh1(step-990000)
    open(unit=1,file=trim(adjustl(f1))//'K-msd.txt')
    do i=1,n
        write(1,'(20(F20.12))')real(bh2(i))/1000.0,(pmsd(j,i),j=1,ntype),msd(i)
    enddo
    close(1)
    open(unit=1,file=trim(adjustl(f1))//'K-isf.txt')
    do i=1,n
        write(1,'(20(F20.12))')real(bh2(i))/1000.0,(pisf(j,i),j=1,ntype),isf(i)
    enddo
    close(1)
    open(unit=1,file=trim(adjustl(f1))//'K-ngf.txt')
    do i=1,n
        write(1,'(20(F20.12))')real(bh2(i))/1000.0,(pngf(j,i),j=1,ntype),ngf(i)
    enddo
    close(1)
enddo
end




































