#2. Devise an experiment to verify that get item and set item are (1) for dictionaries.
# Import the timeit module
import timeit
import random
# Import the Timer class defined in the module
from timeit import Timer

for i in range(1,2000):
    t = timeit.Timer("random.randrange(%d) in x" %1000 
    ,"from __main__ import random,x")
    x = {k: random.random() for k in range(1000)}
    dict_time = t.timeit(number=1000)
    t = timeit.Timer("x[random.randrange(%d) in x] = 1" %1000 
    ,"from __main__ import random,x")
    set_time = t.timeit(number=1000)
    print(" dict_time get operator ::. Time =  ",dict_time)
    print(" set_time get operator ::. Time =  ",set_time)