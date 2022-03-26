from importlib.resources import open_text
from math import perm


n = 5
#f = open_text('')

permutation = list(('5 1 4 2 3').replace(' ', ''))

increasePerm = []
decreasePerm = []
Max = max(permutation)
Min =  min(permutation)

increasePerm.append(Min)
decreasePerm.append(Max)

def Increase(permutation):
    start = permutation.index(Min)
    end = n
    i = start
    while i < n-1:
        tempMin = permutation[i+1]
        for j in range(i+1,end):
            if tempMin>=permutation[j]:
                i=j
                tempMin = permutation[j]

        increasePerm.append(tempMin)
        return increasePerm

#decrease
start = permutation.index(Max)
end = n
i = start

while i < n-1:
    tempMin = permutation[i]
    lista=[]
    for j in range(i+1,end):
        if tempMin>permutation[j]:
            tempMin= permutation[j]
            lista.append(permutation[j])
            i=j
        
    decreasePerm.append(lista)


print(increasePerm(permutation),decreasePerm)



