program runsimulation
implicit none
open(unit=1,file="ret.py")
write(1,"(24A)"),"from dynamics import isf"
close(1)
call system("python2.7 ret.py && rm ret.py")
end
