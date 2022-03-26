def Mendel(k,m,n):
    # I'm going to calculate the probability of the recessive trait
    pop = k + m + n
    Recesstwo = (n/pop)*((n-1)/(pop-1))
    Heterotwo = (m/pop)*((m-1)/(pop-1))
    RecessHetero = (n/pop)*(m/(pop-1)) + (m/pop)*(n/(pop-1))

    probRecess = Recesstwo + (1/4)*Heterotwo + (1/2)*RecessHetero
    # I print the complementary proability to know the probability of dominat trait
    return 1 - probRecess

Result  = round(Mendel(23,21,29), 5)
print(Result)
