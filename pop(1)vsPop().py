# Import the timeit module
import timeit
# Import the Timer class defined in the module
from timeit import Timer

pop_zero = Timer("x.pop(0)","from __main__ import x")
pop_end = Timer("x.pop()","from __main__ import x")

x = list(range(2000000))
print("pop(0) ",pop_zero.timeit(number=10000), "milliseconds")
x = list(range(2000000))
pop_end.timeit(number=1000)
print("pop() ",pop_end.timeit(number=10000), "milliseconds")

