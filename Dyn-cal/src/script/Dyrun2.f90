program cc
implicit none
open(unit=2,file="path4.py")
write(2,"(23A)"),"from dynamics import DY"
close(2)
call system("python2.7 path4.py && rm path4.py")
end
