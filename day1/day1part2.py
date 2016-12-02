input_string = "R4, R3, R5, L3, L5, R2, L2, R5, L2, R5, R5, R5, R1, R3, L2, L2, L1, R5, L3, R1, L2, R1, L3, L5, L1, R3, L4, R2, R4, L3, L1, R4, L4, R3, L5, L3, R188, R4, L1, R48, L5, R4, R71, R3, L2, R188, L3, R2, L3, R3, L5, L1, R1, L2, L4, L2, R5, L3, R3, R3, R4, L3, L4, R5, L4, L4, R3, R4, L4, R1, L3, L1, L1, R4, R1, L4, R1, L1, L3, R2, L2, R2, L1, R5, R3, R4, L5, R2, R5, L5, R1, R2, L1, L3, R3, R1, R3, L4, R4, L4, L1, R1, L2, L2, L4, R1, L3, R4, L2, R3, L1, L5, R4, R5, R2, R5, R1, R5, R1, R3, L3, L2, L2, L5, R2, L2, R5, R5, L2, R3, L5, R5, L2, R4, R2, L1, R3, L5, R3, R2, R5, L1, R3, L2, R2, R1" 

instructions = input_string.split(', ')

direction = 0 # 0 = North, 1 = East, 2 = South, 3 = West
cardinal = ['north', 'east', 'south', 'west']

coords = []

y = 0
x = 0

solution = None

for instruction in instructions:
    if instruction[0] == 'L':
        direction -= 1
    elif instruction[0] == 'R':
        direction += 1

    if direction == -1:
        direction = 3
    elif direction == 4:
        direction = 0

    repetitions = int(instruction[1:])

    for i in xrange(repetitions):
        if cardinal[direction] == 'north':
            y += 1
        elif cardinal[direction] == 'south':
            y -= 1
        elif cardinal[direction] == 'east':
            x += 1
        elif cardinal[direction] == 'west':
            x -= 1

        position = (x, y)

        for coord in coords:
            if position == coord:
                solution = abs(position[0]) + abs(position[1])
                break

        coords.append(position)
        
        if solution:
            break

    if solution:
        break

print solution
