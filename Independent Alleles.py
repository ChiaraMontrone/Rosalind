from math import factorial


k = 5
n = 9
P = 2**k
succes =  0.25
fail = 0.75 
probability = 0

for i in range(n, P + 1):
    prob  = (factorial(P) / (factorial(P - i) * factorial(i))) * (0.25**i) * (0.75**(P - i))
    probability +=  prob

print(round(probability, 3))