import timeit
import random

for i in range(10000,1000001,20000):
    t = timeit.Timer("random.randrange(%d) in x" %i 
    ,"from __main__ import random,x")
    x = list(range(i)) 
    lst_time = t.timeit(number=1000)
    x = {j:None for j in range(i)}
    d_time = t.timeit(number=1000)
    print("%d,%10.3f,%10.3f, timeDict/timeList = %10.3f" % (i, lst_time, d_time,lst_time/d_time))




# 7 Programming Exercises
# 1. Devise an experiment to verify that the list index operator is 𝑂(1).
# 2. Devise an experiment to verify that get item and set item are 𝑂(1) for dictionaries.
# 3. Devise an experiment that compares the performance of the del operator on lists and
# dictionaries.
# 4. Given a list of numbers in random order write a linear time algorithm to find the 𝑘th
# smallest number in the list. Explain why your algorithm is linear.
# 5. Can you improve the algorithm from the previous problem to be 𝑂(𝑛 log(𝑛))