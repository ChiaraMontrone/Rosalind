dna = 'CTGCGTTGGTTGCGTTGATAGATGCGTTGCTACTCCCTGCTATGCGTTGGGTCCCCAGTGCGTTGTGCGTTGATCTGCGTTGTTCTGCGTTGGGTGCGTTGAATGCGTTGTGCGTTGTTGCGTTGAGCCATTTTGCGTTGTTGCGTTGTAAATACTGTCGGCACTTGCGTTGATGCGTTGTGCGTTGCGGAAGTTTAGTGCGTTGAACCCCTGCGTTGTGCGTTGTGCACAAACTGCGTTGCACTGCGTTGTTGCGTTGTCAGGCCAGAGTGCGTTGTGTTGCGTTGCGATGCGTTGAGATGCGTTGCTTTGTATGCGTTGTGCGTTGGTCAACATGCGTTGAACACCACAAATGCGTTGCTCATCGGTGCGTTGCTTGCGTTGTGCGTTGTGCGTTGCTGCGTTGTGCGTTGATGCGTTGCAGTGCGTTGCGGCTGCGTTGTGCGTTGGAGTGCGTTGCGACTGCGTTGCTTGCGTTGTGCGTTGTGGACTTGCGTTGATCTGACCCCCGTCTGCGTTGGTTTGCGTTGTGCGTTGATGCGTTGTGCGCGACACATGGATAGTGCGTTGCGTGCGTTGAATGCGTTGACCTGCGTTGCTGCGTTGCGAATGCGTTGATTGGATGCGTTGCTCTGCGTTGAGAGCCTGCGTTGTGCGTTGTGCGTTGTGCGTTGTGCGTTGTGCGTTGGCAATGCGTTGCGACGTCTTGCGTTGGCCTGCGTTGTGCGTTGCTTGCGTTGACCAGACGTGCGTTGGTCTTGCGTTGATGCGTTGTGCGTTGGCGGTCCTCTAGCGTGCGTTGGGGAAGTGCGTTGTGTGCGTTGTGCGTTGTTGTAACTGTGCGTTGGCG'
substring ='TGCGTTGTG'

start = 0
while True:
    start = dna.find(substring, start)
    if start == -1: break
    print( start+1)
    start += 1
   