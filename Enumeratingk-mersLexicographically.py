from dataclasses import replace
from itertools import combinations_with_replacement, permutations
import itertools

inAlphabeth = 'A B C D E F G'
inPermutaion = 3
output=set()
alphabeth = inAlphabeth.split(' ')

perm = [p for p in itertools.product(alphabeth, repeat=inPermutaion)]

for i in perm:
  output.add(''.join(i))


for out in sorted(output):
  print(out)



