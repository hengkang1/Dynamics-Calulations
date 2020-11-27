program PDFforLAMMPS
implicit none
!****************************************************************************
integer max_atoms,max_types
parameter (max_atoms    =1000000)
parameter (max_types    =10)
!****************************************************************************
integer sp,p,natom,ntype,i,ntyp(max_types),j,k,k0,n,er,ss,smax,ns,temper1,temper2,temper3
integer num(max_types,max_types,2500),idd,num0(2500),typ(max_atoms)
real zb0(max_atoms,3),dis,q,sq(max_types,max_types,2500)
real pdf(max_types,max_types,2500),lx(2500),xb,xe,yb,ye,zb,ze,xl,yl,zl,pdf0(2500),sq0(2500)
real sz,xx,yy,zz,dr,rmax
character*50 f1,f2,f3,f4,f5

!****************************************************************************
open(unit=10,file="input-DP.txt")
read(10,*)temper1,temper2,temper3
do p=temper1,temper2,temper3
write(f1,"(I4)")p
f2=trim(adjustl(f1))//"K-cfg.lammpstrj"
f3=trim(adjustl(f1))//"K-g(r).txt"
f4=trim(adjustl(f1))//"K-sq.txt"
!****************************************************************************
dr=0.01
rmax=25.0
num=0
num0=0
ss=0
!****************************************************************************
open(unit=1,file=f2)
do while(.true.)
   read(1,*,iostat=er)
   if(er/=0)exit
   ss=ss+1
   print*,'The number of configurations is',ss
   read(1,*)
   read(1,*)
   read(1,*)natom
   read(1,*)
   read(1,*)xb,xe
   read(1,*)yb,ye
   read(1,*)zb,ze
   xl=xe-xb
   yl=ye-yb
   zl=ze-zb
   read(1,*)
   ntyp=0
   ntype=1
   do i=1,natom
      read(1,*)idd,typ(idd),(zb0(idd,j),j=1,3)
      if(typ(idd)>ntype)ntype=typ(idd)
      ntyp(typ(idd))=ntyp(typ(idd))+1
   enddo
   close(1)
!****************************************************************************
   smax=10000000/natom
   sz=min(xl/2.0,yl/2.0,zl/2.0)
   if(sz>rmax)sz=rmax
   ns=int(sz/dr)
   sz=real(ns)*dr
!****************************************************************************
   do i=1,natom-1
      do j=i+1,natom
         xx=zb0(i,1)-zb0(j,1)
         yy=zb0(i,2)-zb0(j,2)
         zz=zb0(i,3)-zb0(j,3)
         xx=xx-anint(xx/xl)*xl    !周期性边界条件
         yy=yy-anint(yy/yl)*yl
         zz=zz-anint(zz/zl)*zl
         dis=sqrt(xx*xx+yy*yy+zz*zz)
         if(dis>sz+dr/2.0)cycle
         n=int((dis+dr/2.0)/dr)
         num(typ(i),typ(j),n)=num(typ(i),typ(j),n)+1
         num(typ(j),typ(i),n)=num(typ(j),typ(i),n)+1
         num0(n)=num0(n)+2
     enddo
   enddo
   if(ss+1>smax)exit
enddo
!****************************************************************************
open(unit=2,file=f3)
do k=1,ns
   lx(k)=dr*k
   do i=1,ntype
      do j=i,ntype
         pdf(i,j,k)=num(i,j,k)*xl*yl*zl/ntyp(i)/ntyp(j)/(4*3.1415159265*dr*lx(k)**2)/real(ss)
	  enddo
   enddo
   pdf0(k)=num0(k)*xl*yl*zl/natom/natom/(4*3.1415159265*dr*lx(k)**2)/real(ss)
   write(2,'(36(F11.4))')lx(k),((pdf(i,j,k),j=i,ntype),i=1,ntype),pdf0(k)
enddo
close(2)
!****************************************************************************
open(unit=3,file=f4)
do k0=1,ns
   q=k0*dr
   do k=1,ns
   lx(k)=dr*k
      do i=1,ntype
	     do j=i,ntype
		    sq(i,j,k0)=sq(i,j,k0)+(pdf(i,j,k)-1)*4*3.14*lx(k)*dr*sin(q*lx(k))/q 
		 enddo
	  enddo
	  sq0(k0)=sq0(k0)+(pdf0(k)-1)*4*3.14*lx(k)*dr*sin(q*lx(k))/q 
    enddo
write(3,'(36(F11.4))')q,((natom/xl/yl/zl*sq(i,j,k0)+1.0,j=i,ntype),i=1,ntype),natom/xl/yl/zl*sq0(k0)+1.0
enddo
!****************************************************************************   
close(3)
end do 
end


