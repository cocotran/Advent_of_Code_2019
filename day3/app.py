input_1 = open("input1.txt", "r")
input_2 = open("input2.txt", "r")

wire_1 = [i for i in input_1.read().split(',')]
wire_2 = [i for i in input_2.read().split(',')]

def draw_wire_map(path: list):
    current_x = current_y = step = 0
    directions = {'R': (1,0), 'L': (-1,0), 'U': (0,1), 'D': (0,-1)}
    coordinate = {}
    for i in path:
        direction_x, direction_y = directions[i[0]]
        for distance in range(int(i[1:])):
            current_x += direction_x
            current_y += direction_y
            step += 1
            if (current_x, current_y) not in coordinate:
                coordinate[(current_x, current_y)] = step
    return coordinate

def manhattan_distance(num: tuple):
    return (abs(num[0]) + abs(num[1]))

wire_1_coordinate = draw_wire_map(wire_1)
wire_2_coordinate = draw_wire_map(wire_2)
intersection = [i for i in wire_1_coordinate if i in wire_2_coordinate]

distance = []
for i in intersection:
    distance.append(manhattan_distance(i))

print(min(distance))

part2 = min(wire_1_coordinate[point] + wire_2_coordinate[point] for point in intersection)
print(part2)