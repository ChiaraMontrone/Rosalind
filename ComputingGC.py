from Bio import SeqIO

CG = 0 
Dict = dict()
for seq_record in SeqIO.parse("c:/Users/Utente/Desktop/Università/PoCS2/Rosalind 1/rosalind_gc(3).fasta", "fasta"):
    for nucleotide in seq_record:
        if nucleotide == 'C':
            CG += 1
        if nucleotide == 'G':
            CG += 1
           
    per = ((CG/len(seq_record))*100)
    Dict[seq_record.id] = per
    CG = 0 


all_per = Dict.values() #to get the max value of the dictionary
per_max = max(all_per)

#print key and value required
for key,value in Dict.items():
    if value == per_max:
         print(key, per_max)
