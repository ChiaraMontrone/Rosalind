from dataclasses import replace


triple = dict()

triple = {'TTT':'F',
'CTT':'L',
'ATT':'I',
'GTT':'V',
'TTC':'F',
'CTC':'L',
'ATC':'I',
'GTC':'V',
'TTA':'L',
'CTA':'L',
'ATA':'I',
'GTA':'V',
'TTG':'L',
'CTG':'L',
'ATG':'M',
'GTG':'V',
'TCT':'S',
'CCT':'P',
'ACT':'T',
'GCT':'A',
'TCC':'S',
'CCC':'P',
'ACC':'T',
'GCC':'A',
'TCA':'S',
'CCA':'P',
'ACA':'T',
'GCA':'A',
'TCG':'S',
'CCG':'P',
'ACG':'T',
'GCG':'A',
'TAT':'Y',
'CAT':'H',
'AAT':'N',
'GAT':'D',
'TAC':'Y',
'CAC':'H',
'AAC':'N',
'GAC':'D',
'TAA':'Stop',
'CAA':'Q',
'AAA':'K',
'GAA':'E',
'TAG':'Stop',
'CAG':'Q',
'AAG':'K',
'GAG':'E',
'TGT':'C',
'CGT':'R',
'AGT':'S',
'GGT':'G',
'TGC':'C',
'CGC':'R',
'AGC':'S',
'GGC':'G',
'TGA':'Stop',
'CGA':'R',
'AGA':'R',
'GGA':'G',
'TGG':'W',
'CGG':'R',
'AGG':'R',
'GGG':'G'}


dna = 'CCAAATCGCTGTGGATGTTTCACCCGGTTAATTCCACCTACGATGAGCGCTGAACCACTGACACGAGACAAATACTCTTCGCCTGCTCCACTGAAAACCGCCGGTGTCTCAAGAAATCAGTAGCAGGGAGCAACTTACTATAAACTTCCTAACTTTGAAGTCGCTCCATTTTCTGGGTGAAGGACCCATAGATGGTTGAGTATTTACAGCACAGAGGTATTAAGCTCGGAGACATCTCAGTGATAACAACATCCGCACGCCTACCAGCCCGTAAGTTTCTAGAATGCCCGGCCAAGCTATATTACATGTCCAAACAGATAAACAAATGTTACTTGAACAACCGAGAGGATGCTATCCAAGCTAAATCCTGAAGCTTTAAGACCTGAGAACCGGACCACTGAATAGAGTCCGCTAAATGGGGGTGTGGAGAGGATAGCTATCCTCTCCACACCCCCATGGAACACCGCTAGTTCCCGAACGGACTGCAAAGCTTGATTATGGGACAAAGAACGAAAGTAAACTTTATTTCTACACATCTGAACCGATAGCTGCTTGGCCACCGTCACTCGAGGCTACCAGTATCTAGCCATTCATTGCTACTGACACACTGGTTTCGCGTGTAGCGCAATACGTCGACCCGCTTGGTCGCCAGAGGGATCAACAACGTCTCTTTGTTTGGGCCCCCGTTGTGCGTTGTTTAGACCCTAAATCACCCAGGATTCAGTCGTGATTGCTCATTTTCGAGTTACCAATAGTCCTATTATTCGTGAAATAGATTACCGTTCGGAATTAGTATACGGACACAGAACGCGCATCTCGTAGTCAATGAACTCTTGTTTTGACATAGTGAAAGCGTTCACAGCTAACTGTTT'


def ORF (dna):                  
    n = 0
    out = ''
    len_dna = len(dna)
    out_dna = []
    while n <= len_dna: 
        substring = dna[n:n+3]              
        value = triple.get(substring)                          # make the codon
    
        if substring == 'ATG':                                 # find the start codon
            for i in range(n,len_dna,3):
                value_triple = triple.get(dna[i:i+3])
                if value_triple == "Stop":                     # stop when find the stop codon
                    break
                if value_triple:
                    out += value_triple
            if value_triple and value_triple  =="Stop":
                out_dna.append(out)                            # crate a list of all the ORFs
            out=''
        n += 1
    return out_dna

def Complement (dna):                                           # make the complemant strand of dna
    new_dna = ''
    for nucleotide in dna:
        if nucleotide == 'T':
            new_dna += 'A'
        if nucleotide == 'C':
            new_dna += 'G'
        if nucleotide == 'A':
            new_dna += 'T'    
        if nucleotide == 'G': 
            new_dna += 'C'
    
        dna  = new_dna                        
    return dna


print('\n'.join(set(ORF(dna)+ORF(Complement(dna[::-1])))) )

        


