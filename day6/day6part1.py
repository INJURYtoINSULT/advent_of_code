from collections import Counter
i = 0
decrypted = ""

for i in range(8):
    column = []
    f = open('day6.txt', 'r')
    for line in f.readlines():
        if len(line) > 2:
            column += line[i]
    
    cnt = Counter(column)
    decrypted += cnt.most_common(1)[0][0]
print decrypted
    
