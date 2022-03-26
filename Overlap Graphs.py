from Bio import SeqIO


for seq_record in SeqIO.parse("C:/Users/Chiara/Downloads/rosalind_grph.fasta","fasta"):
    for seq_record2 in SeqIO.parse("C:/Users/Chiara/Downloads/rosalind_grph.fasta","fasta"):
        k = 3
        last = seq_record [-k : ] 
        first = seq_record2 [:k ]
        if first.seq    == last.seq:
            if seq_record.id != seq_record2.id:
                print(seq_record.id + ' '+seq_record2.id)
    
   