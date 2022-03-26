from Bio import SeqIO    

record = SeqIO.read('C:/Users/Chiara/OneDrive/notebook/Università/PoCS2/Rosalind 2/rosalind.fasta', 'fasta')
dna = str(record.seq)
dnaReverse = str(record.seq.complement())                   # Creation of complement of the entire DNA seq

for i in range(len(dna)):
    for j in range(i,len(dna)):
        nucleotide = dna[i:j+1]
        reverseNuc = dnaReverse[i:j+1]
        if len(nucleotide) >= 4 and len(nucleotide) <= 12:  # Range of lenght of reverse palindrome seq
            if nucleotide == reverseNuc [::-1]:
                print(i+1, len(nucleotide))

