file = open('C:/Users/Chiara/OneDrive/notebook/Università/PoCS2/Rosalind 2/rosalind.fasta', 'r')
nodes = ' '
listNode = []
while (nodes != ''):
    nodes = file.readline().strip()             # read each line and remove the spaces
    listNode.append(nodes)
listNode.remove('')

n = int(listNode[0])
edges = n - len(listNode)

print(edges)