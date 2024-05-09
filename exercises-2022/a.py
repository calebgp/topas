def manhattan_distance(a1, r1, a2, r2):
    return abs(a1 - a2) + abs(r1 - r2)


hanno_line = input()
hanno_a, hanno_r = map(int, hanno_line.split())
kandula_line = input()
kandula_a, kandula_r = map(int, kandula_line.split())
distance = manhattan_distance(hanno_a, hanno_r, kandula_a, kandula_r)
print(distance)
