program runsimulation
implicit none
open(unit=1,file="path.py")
write(1,"(27A)"),"from dynamics import SAMPLE"
close(1)
call system("python2.7 path.py && rm path.py")
end
