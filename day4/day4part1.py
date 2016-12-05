import collections
f = open('day4.txt', 'r')
sector_sum = 0

for i in f.readlines():
    line = i.split('[')
    encryption = line[0]
    if len(encryption) < 2:
        break
    checksum = line[1].replace("]\n", '')
    sector_id = ""
    cnt = collections.Counter()

    for char in encryption:
        if char.isdigit():
            sector_id += char

    checksum_test = ""

    for pos, char in enumerate(encryption):
        cnt[char] += 1

    cnt = cnt.items()
    for pos, counter_char in enumerate(cnt):
        #current = None
        #previous = None
        #current = counter_char
        most_common = sorted(cnt, key=lambda pair: (-pair[1], pair[0]))
        if most_common[pos][0].isalpha():
            checksum_test += most_common[pos][0]
        if len(checksum_test) == 5:
            break

    if checksum == checksum_test:
        sector_sum += int(sector_id)
    cnt = ()
print sector_sum
