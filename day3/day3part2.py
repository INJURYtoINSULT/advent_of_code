f = open('day3_input.txt', 'r')
row = []
ldimensions = []
mdimensions = []
rdimensions = []
possible = 0

for line in f.readlines():
    row = line.split()
    if len(row) > 0:
        ldimensions.append(row[0])
        mdimensions.append(row[1])
        rdimensions.append(row[2])

        if len(ldimensions) == 3 and len(mdimensions) == 3 and len(rdimensions) == 3:
            if (int(ldimensions[0]) + int(ldimensions[1]) > int(ldimensions[2]) and
            int(ldimensions[0]) + int(ldimensions[2]) > int(ldimensions[1]) and
            int(ldimensions[1]) + int(ldimensions[2]) > int(ldimensions[0])):
                possible += 1
            if (int(mdimensions[0]) + int(mdimensions[1]) > int(mdimensions[2]) and
            int(mdimensions[0]) + int(mdimensions[2]) > int(mdimensions[1]) and
            int(mdimensions[1]) + int(mdimensions[2]) > int(mdimensions[0])):
                possible += 1
            if (int(rdimensions[0]) + int(rdimensions[1]) > int(rdimensions[2]) and
            int(rdimensions[0]) + int(rdimensions[2]) > int(rdimensions[1]) and
            int(rdimensions[1]) + int(rdimensions[2]) > int(rdimensions[0])):
                possible += 1

            row = []
            ldimensions = []
            mdimensions = []
            rdimensions = []
    else:
        break
print possible
