from Bio import SeqIO


def Translating(rna):
    triple = dict()

    triple = {
        'TTT': 'F',     'CTT': 'L',     'ATT': 'I',     'GTT': 'V',
        'TTC': 'F',     'CTC': 'L',     'ATC': 'I',     'GTC': 'V',
        'TTA': 'L',     'CTA': 'L',     'ATA': 'I',     'GTA': 'V',
        'TTG': 'L',     'CTG': 'L',     'ATG': 'M',     'GTG': 'V',
        'TCT': 'S',     'CCT': 'P',     'ACT': 'T',     'GCT': 'A',
        'TCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
        'TCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
        'TCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
        'TAT': 'Y',     'CAT': 'H',     'AAT': 'N',     'GAT': 'D',
        'TAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
        'TAA': 'Stop',     'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
        'TAG': 'Stop',     'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
        'TGT': 'C',     'CGT': 'R',     'AGT': 'S',     'GGT': 'G',
        'TGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
        'TGA': 'Stop',     'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
        'TGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
    }

    n = 0
    out = ""

    while True:
        substring = rna[n:n+3]
        value = triple.get(substring)
        #if not value ==
        if not value or value == "Stop" or n > len(rna): break
        n += 3
        out = out + value
    return out

def readfile(filename):

    file = open(filename, "r")
    sequences = []
    result = ""       
    
    for line in file:
        if ">" in line:
            sequences.append(result)
            result = ""
        else:
            if "\n" in line:
                result += line[:len(line) - 1]
            else:
                result += line
    sequences.append(result)
    sequences.remove('')
    return sequences
    
lenght =[]
rna = ''
subseq = []
sequenze =readfile("C:/Users/Chiara/OneDrive/notebook/Università/PoCS2/Rosalind 2/rosalind.fasta")

for seq_record in sequenze:
    lenght.append(len(seq_record))
    
maxseq= max(lenght)
for var in sequenze:
    if len(var)== maxseq:
        rna= var
    else:
        subseq.append(var)
for subvar in subseq:
    rna = str.replace(rna,subvar,'')


print (Translating(rna))