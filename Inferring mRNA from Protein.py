AminoAcid =  dict()
AminoAcid = {'A' : 4,
'C' : 2,
'D' : 2,
'E' : 2,
'F' : 2,
'G' : 4,
'H' : 2,
'I' : 3,
'K' : 2,
'L' : 6,
'M' : 1,
'N' : 2,
'P' : 4,
'Q' : 2,
'R' : 6,
'S' : 6,
'T' : 4,
'V' : 4,
'W' : 1, 
'Y' : 2}

m = 1000 
i = 1

protein = 'MKYKDPCCTNLWSDMNKDNAWWFSGCCPFNGNVDYGFKAQVCGRINTHQGVDGQRNSSYYTFTPCHCYWENCRTGDNGTPTDFHHQLVHFHCGCVHEPLVQTWCSNHNNRIWWRCRGHQFGVRARWAVPWQQAHWFRPKIFAKDMLLDMCGRLTCPWYLDFHYPVQRPSKRMPEECMTELDGETFNTKTPQWQDYHQNGYWVIKEDMCRIEVKRVQDPGAQQWQPMAENKSHSSMGVFMMPLPWRMEMEGATQGHMPKWNKCRRSYHSWLQCICTSNFVCHGCSLSSYGRDIIVYIIQADWLTCYISVFLFKDYLELPGECYYFHTYRTALATCHRFLFAYWLCVQQPWWDGHQAFFVVPRTCWGCAGEIRDPICSGVEHQFHTHGTQMWCSDNRVQDVGCALADQTHETDCELCYDVCGLDWDGFWQSGKAYRPHGFITVYMIMMRNIICNTWWEYYRNMLSTNFNQIYFQLYGPCPYAEFMQILLVNYDEVQAPIEWKEPIYIQTWCNVARTTMPFCWILWGVDRKSGSCAPVGAECWEWERVIMDKANLHICSWMFADKIDTATPFGKWQQHNGNREQEVSQWHFIHTGQKYPKTCLAVQICNKFVKNERKDEEWSITMQCITDMAFFHISTSPRWDVYEQQEMSIFRPMPQWGPKLPCRLERHDDYLKLPHANICYKFGWSLHFSAIRPKFHKESWNGRHPFHWQYPSTHVCYMQDMTGVDFWQRHKYMGMKTRIYPYCYNLAFYGRTICIDGNNLCPNDGEAQNRGFDKFPWFEFKEEEKLVYIAGMAVYFRTQCACENNNVRWQDNEPQYLAQNNMFPSQLHKCGERRQVHMTLFPHGTPILHCKPKKSTRTGKWCHIWQIISMCLDEPWHAYTGHDYKHTHKDSPEYNKPTEYCIFPDIISSGAPCAWMTSCKNFIDRWKTWNYRDFDSNHMFHKVVGAMGWYRSAYMHQAQQPQWYIRNPDMVNPKMDKHIEMTHAVFMNALEKDQFSR'
stop  = 3

for amino in protein:
    aminos = AminoAcid[amino] 
    i = (i*aminos)

i = i * stop

print (i % 1000000)


