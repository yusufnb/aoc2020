import re
with open('./day2-input.txt') as f:
    lines = f.read().splitlines()

pat = re.compile("^([0-9]+)-([0-9]+) ([a-z]+): ([a-z]+)$")

part1 = 0
part2 = 0
for rule in lines:
    m = pat.match(rule)
    print(rule)
    if m is not None:
        start = int(m.group(1))
        end = int(m.group(2))
        c = m.group(3)
        str = m.group(4)

        count = len(str.split(c)) - 1

        if (count >= start and count <= end):
            part1 = part1 + 1

        startChar = str[start-1]
        endChar = str[end-1]

        if ((startChar == c and endChar != c) or (startChar != c and endChar == c)):
            part2 = part2 + 1


print (part1)
print(part2)