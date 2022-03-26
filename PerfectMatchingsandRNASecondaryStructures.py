from math import factorial


RNA  = 'ACCCUAUUGGAACAUUUCGGGACAAGCUAAACGUUUCCCGCAGCUAAGUGUGAGGCGGAGUUGUCCCCUA'
A = 0
U = 0
G = 0
C = 0
AU = 0
CG = 0 

for nucleotide in RNA:

    if nucleotide == 'A':
        A += 1
    if nucleotide == 'U':
        U += 1
    if nucleotide == 'C':
        C += 1
    if nucleotide == 'G':
        G += 1

AU =  min(A,U)
CG = min(C,G)


print(factorial(AU) * factorial(CG))


