import re


with open('./day7-input.txt') as f:
    lines = f.read().splitlines()

def get_color(str):
    str = str.strip(" ")
    matches = re.match("^([0-9]+ *)?(.+) bags?\.?$", str)
    if matches is None:
        print ("Error", str)
    return matches.group(2)

def get_color_count(str):
    str = str.strip(" ")
    matches = re.match("^([0-9]+) (.+) bags?\.?$", str)
    if matches is None:
        return {"color": "None", "count": 0}
    else:
        return {"color": matches.group(2), "count": int(matches.group(1))}

def part1():
    stack = set(cp.get(lookup))
    bags = set(cp.get(lookup))
    while(len(stack) > 0):
        str = stack.pop()
        if str in cp:
            parents = set(cp[str])
            if len(parents) > 0:
                bags.update(parents)
                stack.update(parents)

    print len(bags)

def get_count(color):
    if color in pc:
        total = 1
        prt = [color]
        for x in pc[color]:
            cnt = get_count(x["color"])
            total = total + x["count"] * cnt
        return total
    else:
        return 0

cp = {}
pc = {}

for line in lines:
    parts = line.split("contain")
    p = get_color(parts[0])
    children = [get_color(i) for i in parts[1].split(",")]
    pc[p] = [get_color_count(i) for i in parts[1].split(",")]
    for c in children:
        if c not in cp:
            cp[c] = set()
        cp[c].add(p)

lookup = "shiny gold"
no_bag = "no other"
part1()

print "part 2"
print get_count(lookup)-1