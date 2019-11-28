


def verifyMultiply(a,b):
    divisores = []
    for i in range(len(a)):
        for j in range(len(b)):
            x = [a[i], b[j]]
            div = (max(x))%(min(x))
            divisores.append(max(x)/min(x))
            if div != 0:
                return divisores,False
    return divisores,True

def filterNumber(arrayA,arrayFilter):
    filteredArray = []
    #convert the set to a list
    listArrayFi = list(arrayFilter)
    for i in range(len(listArrayFi)):
        if listArrayFi[i] >= max(arrayA):
            filteredArray.append(listArrayFi[i])
    return filteredArray

def getAllDivisor(filteredArray,arrayC,long2):
    arrayDivisor=[]
    for i in range(len(filteredArray)):
        contadorDivs = 1
        for j in range(len(arrayC)):
            x = [arrayC[j], filteredArray[i]]
            print(x,"----",max(x)%min(x))
            if max(x)%min(x) == 0:
                contadorDivs += 1
        print("contadorDivs",contadorDivs)
        if contadorDivs==long2:
            arrayDivisor.append(filteredArray[i])
    return arrayDivisor
                




a = [2]
b = [20, 30,12]

if(verifyMultiply(a,b)[1]==True):
    setList = set(verifyMultiply(a,b)[0])
    print(setList)
    filterList = filterNumber(a,sorted(setList))
    print(filterList)
    divisorOk = getAllDivisor(filterList,a+b,len(a+b))
    print(divisorOk)
else:
    print(str(0))


