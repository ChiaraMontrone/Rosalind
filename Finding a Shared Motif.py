from Bio import SeqIO

dna=[]
for seq_record in SeqIO.parse("C:/Users/Chiara/OneDrive/notebook/Università/PoCS2/Rosalind 2/rosalind.fasta","fasta"):
    dna.append(seq_record.seq)

mindnaIndex = dna.index(min(dna, key=len))

mindna = dna[mindnaIndex]
commonSubstring =''

for i in range(len(mindna)):
    n = 0
    present = True
    while present:

        for dnarecord in dna:
            if mindna[i:i+n] not in dnarecord or n>1000:
                present = False
                break
        if present:
            commonSubstring = max(mindna[i:i+n], commonSubstring, key=len)
        n += 1
print(commonSubstring)
