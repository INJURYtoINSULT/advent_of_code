f = open('day3_input.txt', 'r')
dimensions = []
possible = 0

for line in f.readlines():
    dimensions = line.split()
    if len(dimensions) > 0:
        if (int(dimensions[0]) + int(dimensions[1]) > int(dimensions[2]) and
        int(dimensions[0]) + int(dimensions[2]) > int(dimensions[1]) and
        int(dimensions[1]) + int(dimensions[2]) > int(dimensions[0])):
            possible += 1
    dimensions = []
print possible
