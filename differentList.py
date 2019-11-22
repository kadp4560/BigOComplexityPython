# Import the timeit module
import timeit
# Import the Timer class defined in the module
from timeit import Timer
#
def test0():
    pass

def test1():
    l = []
    for i in range (1000):
        l = l + [i]

def test2():
    l = []
    for i in range(1000):
        l.append(i)

def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))


# If the above line is excluded, you need to replace Timer with
# timeit.Timer when defining a Timer object
t0 = Timer("test0()", "from __main__ import test0")
t0Time = t0.timeit(number=10000)
print("concat times it takes to call a function =  ",t0Time, "milliseconds")


t1 = Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=10000)-t0Time, "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=10000)-t0Time, "milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=10000)-t0Time, "milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=10000)-t0Time, "milliseconds")
