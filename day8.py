import re

with open('./day8-input.txt') as f:
    lines = f.read().splitlines()

is_success = False

def xec(ptr, acc, ops, change):
    global is_success
    if is_success == True:
        return

    if ptr == change:
        return

    if ptr == len(lines):
        is_success = True
        print ("Success", acc, ops, change)
        return

    if ptr < 0 or ops > len(lines)+1:
        print ("Failed", acc, ops, change)
        return

    matches = re.match("^(.+) (.[0-9]+)$", lines[ptr])
    if matches is None:
        return

    ins = matches.group(1)
    val = int(matches.group(2))

    if (ins == "nop"):
        xec(ptr + 1, acc, ops+1, change)
        if (change == -1):
            xec(ptr + val, acc, ops+1, ptr)
    elif (ins == "acc"):
        xec(ptr + 1, acc + val, ops+1, change)
    elif ins == "jmp":
        xec(ptr + val, acc, ops+1, change)
        if (change == -1):
            xec(ptr + 1, acc, ops+1, ptr)

def dfs(ptr):
    while True:
        if ptr >= len(lines):
            print ("Success", acc)
        if ptr < 0 or lines[ptr] == 'end':
            break

        matches = re.match("^(.+) (.[0-9]+)$", lines[ptr])
        if matches is None:
            print "None"
            print (ptr, lines[ptr])
            break

        ins = matches.group(1)
        val = int(matches.group(2))
        curr = ptr

        if (ins == "nop"):
            ptr = ptr + 1
        elif (ins == "acc"):
            ptr = ptr + 1
            acc = acc + val
        elif ins == "jmp":
            ptr = ptr + val

        lines[curr] = "end"

xec(0, 0, 0, -1)

# bit hacky, found the line where change needed to be made and recomputed with data change