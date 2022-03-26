import sys 
import requests

url = 'https://www.uniprot.org/uniprot/'
 
with open("C:/Users/Chiara/OneDrive/notebook/Università/PoCS2/Rosalind 2/rosalind.fasta") as file:      
    seqIDs = file.read().replace("\n", " ").split()             # read the file 
sequences = {}


for proID in seqIDs:                                            # get the file from database
    goToURL = url+proID+".fasta"
    response = requests.get(goToURL)
    sequences[proID] = (response.text.split("\n"))
    sequences[proID] = "".join(sequences[proID][1::])

def N_gly_motif(ID, sequence):                                   # identity of what we are searching
    sequence = list(sequence)
    global result
    result = []
    for i in range(0, len(sequence)-3):
        seq = sequence[i:i+4]
        if (seq[0] == "N") and  (seq[1]!= "P") and  (seq[2] == "S" or seq[2] == "T") and (seq[3] != "P"):   # transaltion of 'N{P}[ST]{P}'
            result.append(i+1)

for key, value in sequences.items():                            # serching N-glycosylation motif in the seq given
    N_gly_motif(key, value)
    if not result:
        continue
    else:
        print(key)
        print(*result)

