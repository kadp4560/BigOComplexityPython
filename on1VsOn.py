# Write two Python functions to find the minimum number in a list. The first function should
# compare each number to every other number on the list. 𝑂(𝑛**2)
# 2
# ). The second function should be
# linear 𝑂(𝑛).
import time
# first function find the minimun number  𝑂(𝑛**2)
def findMinON2(listNumbers):
    start = time.time()
    min = listNumbers[0]
    for i in range(0,len(listNumbers)-1):
            for j in range (0,len(listNumbers)-1):
                if listNumbers[i] < min and listNumbers[i] < listNumbers[j] : 
                    min = listNumbers[i]
    end  = time.time()
    print ("Time On2 = %10.25f" %(end- start))
    return min

def findMinON1(listNumbers):
    start = time.time()
    min = listNumbers[0]
    for i in range(0,len(listNumbers)-1):
        if listNumbers[i] < min : 
            min = listNumbers[i]
    end  = time.time()
    print ("Time On1 = %10.25f" %(end- start))
    return min


listNumbers = [5,4,2,4,123,2,4,3,4,5,10,12,45,2,3,4,5,6,7,8,2,1]


print("Minimun With Cuadratic O(N) = ",findMinON2(listNumbers))
print("Minimun With Linear O(N) = ",findMinON1(listNumbers))
