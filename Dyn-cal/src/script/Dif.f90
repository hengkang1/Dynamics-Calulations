program runsimulation
implicit none
open(unit=1,file="dif.py")
write(1,"(29A)"),"from dynamics import diff_fit"
close(1)
call system("python2.7 dif.py && rm dif.py")
end
