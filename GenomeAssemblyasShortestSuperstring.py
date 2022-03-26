from xmlrpc.client import MININT
from Bio import SeqIO

str0=""
def compareTo(self, that):
    return ((self > that) - (self < that))

def findOverlappingPair( str1, str2):
    max = MININT
    len1 = len(str1)
    len2 = len(str2)
    str0=''
    for i in range(1,min(len1, len2)):
        if compareTo(str1[len1 - i:] ,str2[0: i])==0 :
            if (max < i):
                max = i
                str0 = str1 + str2[i:]

    for i in range(1, min(len1, len2)):
        if compareTo(str1[0: i],str2[len2 - i:])==0:
            if (max < i):
                max = i
                str0 = str2 + str1[i:]

    return max,str0

def findShortestSuperstring(arr,  lenght):
		
    while (lenght != 1):
        max = MININT
        l = 0
        r = 0
        resStr = ""
        for i in range(0,lenght-1):
            for j in range(i + 1,lenght):
                res,str0 = findOverlappingPair(arr[i], arr[j])

                if (max < res):
                    max = res
                    resStr = str0
                    l = i
                    r = j
        
        lenght-=1
        

        if (max == MININT):
            arr[0] += arr[lenght]
        else:
            arr[l] = resStr
            arr[r] = arr[lenght]

    return arr[0]
	
arr = [] # ["ATTAGACCTG", "CCTGCCGGAA", "AGACCTGCCG", "GCCGGAATAC" ]
for seq_record in SeqIO.parse('C:/Users/Chiara/OneDrive/notebook/Università/PoCS2/Rosalind 2/rosalind.fasta', 'fasta'):
    arr.append(str(seq_record.seq))




lenght = len(arr)

print(findShortestSuperstring(arr, lenght))