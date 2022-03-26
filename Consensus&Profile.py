from Bio import SeqIO
    
Am = []         
Tm = []
Gm = []
Cm = []
n = 0
seq=[]
for seq_record in SeqIO.parse("C:/Users/Chiara/OneDrive/notebook/Università/PoCS2/Rosalind 2/rosalind.fasta","fasta"):
    seq.append(seq_record)

for x in range(0,len(seq[0])):
    A = 0
    T = 0 
    C = 0  
    G = 0 
    for i in seq:
        nucleotide = i[x]
        if nucleotide == 'C':
                C += 1
        elif nucleotide == 'G':
                G += 1
        elif nucleotide== 'A':
                A += 1
        else:
                T += 1

    Am.append(A)
    Tm.append(T)
    Gm.append(G)
    Cm.append(C)
    

profile = ''
for j in range(0, len(Am)):
    maxval = max(Am[j],Cm[j],Gm[j],Tm[j])
    if maxval == Am[j]:
        profile = profile +'A'
    elif maxval == Tm[j]:
        profile = profile +'T'
    elif maxval == Cm[j]:
        profile = profile +'C'
    else:
        profile = profile +'G'


print(profile)
print('A:', *Am)
print('C:', *Cm)
print('G:', *Gm)
print('T:', *Tm)

