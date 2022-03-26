from math import factorial


def toString(List):                     # function that crate a string from a single number
    return ' '.join(List)

def permute(a, l, r):                   # Function to print permutations of string
    if l==r:
        print (toString(a))
    else:
        for i in range(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l]     # backtrack

numb = 7                                # number of permutation
string =''
for i in range(1,numb+1):
  string += str(i) 
n = len(string)
a = list(string)

print (factorial(numb))
permute(a, 0, n-1)

