with open('./day3-input.txt') as f:
    map = f.read().splitlines()

def part1(map):
    trees = 0
    y = 2
    x = 1
    while y < len(map):
        if x >= len(map[y]):
            x = x - len(map[y])
        if map[y][x] == "#":
            trees = trees + 1
        print (y, x, map[y])
        y = y + 2
        x = x + 1

    print(trees)

part1(map)
