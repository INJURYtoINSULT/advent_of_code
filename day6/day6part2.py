from collections import Counter
i = 0
decrypted = ""

for i in range(8):
    column = []
    f = open('day6.txt', 'r')
    for line in f.readlines():
        if len(line) > 2:
            #print line[i]
            column += line[i]
    
    cnt = Counter(column)
    n = len(cnt.most_common())
    decrypted += cnt.most_common(100)[:-n:-1][0][0]
print decrypted
    
