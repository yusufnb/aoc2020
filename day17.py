import numpy as np
import itertools

with open('./day17-input.txt') as f:
    lines = f.read().splitlines()

def to_input(lines):
    plane = []
    for str in lines:
        plane.append([int(e.replace(".","0").replace("#","1")) for e in str])

    return [plane]

def get_neighbors(input, pos):
    x = [pos.x - 1, pos.x, pos.x+1]
    y = [pos.y - 1, pos.y, pos.y+1]
    z = [pos.z - 1, pos.z, pos.z+1]
    for x1 in x:
        for y1 in y:
            for z1 in z:
                pass


def cycle(input):
    data = np.pad(input, 1, constant_values=0)
    toggle = []
    print (data)
    for (x,x_a) in enumerate(data):
        for (y, y_a) in enumerate(x_a):
            for (z, v) in enumerate(y_a):
                print(v)


input = to_input(lines)
cycle(input)

