n =  82
k = 9
par_perm = 1

for i in range(k):
    par_perm *= (n - i)

out = par_perm % 1000000

print(out)