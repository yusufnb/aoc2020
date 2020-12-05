import re

with open('./day5-input.txt') as f:
    lines = f.read().splitlines()

def getSeatID(str):
    # B = 1, F = 0, R = 1, L = 0
    return int(re.sub("[FL]","0",re.sub("[BR]","1",str)),2)

seats = map(getSeatID, lines)
seats.sort()
for i, x in enumerate(seats):
    if (i == 0 or i == len(seats) - 1):
        continue
    tag = ""
    if (seats[i-1] != x-1 or seats[i+1] != x+1):
        tag = "x"

    print (i, x, tag)

