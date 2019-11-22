# 1. Devise an experiment to verify that the list index operator is 𝑂(1).
# Import the timeit module
import timeit
import random
# Import the Timer class defined in the module
from timeit import Timer

for i in range(1,2000):
    t = timeit.Timer("random.randrange(%d) in x" %1000 
    ,"from __main__ import random,x")
    x = list(range(1000)) 
    lst_time = t.timeit(number=1000)
    print(" list index operator ::. Time =  ",lst_time)




