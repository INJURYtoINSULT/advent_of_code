import collections
f = open('day4.txt', 'r')

for i in f.readlines():
    line = i.split('[')
    encryption = line[0]
    if len(encryption) < 2:
        break
    checksum = line[1].replace("]\n", '')
    sector_name = ""
    sector_id = ""
    cnt = collections.Counter()

    for char in encryption:
        if char.isalpha():
            sector_name += char
        elif char.isdigit():
            sector_id += char
        elif char == '-':
            sector_name += ' '

    caesar = int(sector_id) % 26
    shifted = ""
    checksum_test = ""

    for pos, char in enumerate(encryption):
        cnt[char] += 1

    cnt = cnt.items()
    for pos, counter_char in enumerate(cnt):
        most_common = sorted(cnt, key=lambda pair: (-pair[1], pair[0]))
        if most_common[pos][0].isalpha():
            checksum_test += most_common[pos][0]
        if len(checksum_test) == 5:
            break
    if checksum_test == checksum:
        for char in sector_name:
            if char == ' ':
                shifted += ' '
            elif ord(char) - ord('a') + caesar > 25:
                wrap = ord(char) + caesar - ord('a')
                wrap = wrap % 26
                shifted_char = ord('a') + wrap
                shifted += chr(shifted_char)
            else:
                shifted_char = ord(char) - ord('a') + caesar
                shifted_char = shifted_char + ord('a')
                shifted += chr(shifted_char)
        print shifted, sector_id
