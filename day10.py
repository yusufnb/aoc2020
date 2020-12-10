with open('./day10-input.txt') as f:
    lines = f.read().splitlines()

lines = [int(i) for i in lines]
lines.append(0)
lines.sort()

count = 0

def dfs(i):
    global count
    if (i==len(lines) - 1):
        count = count + 1
        return

    if (i < len(lines) - 1 and lines[i+1] <= lines[i] + 3):
        dfs(i+1)
    if (i < len(lines) - 2 and lines[i+2] <= lines[i] + 3):
        dfs(i+2)
    if (i < len(lines) - 3 and lines[i+3] <= lines[i] + 3):
        dfs(i+3)

dfs(0)
print(count)


