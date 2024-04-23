def read_drawer_unit():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(input())
    return arr


def calc_locked_drawers(drawers):
    locked_drawers = 0
    for i in range(len(drawers)):

        drawer = drawers[i]
        if i != 0:
            previous_drawer = drawers[i - 1]
        else:
            previous_drawer = ""
        if previous_drawer == "#" or drawer == "#":
            locked_drawers += 1
    return locked_drawers


print(calc_locked_drawers(read_drawer_unit()))
