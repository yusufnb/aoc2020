import re

with open('./day6-input.txt') as f:
    lines = f.read().splitlines()

# ["abc", "a"]
def get_yes(ans):
    str = "".join(ans)
    str_set = set([x for x in str])
    return len(str_set)

# list(set(a) & set(b))
def get_yes_intersect(ans):
    intersect = None
    for i in ans:
        ans_set = set([x for x in i])
        if intersect is None:
            intersect = ans_set
        else:
            intersect = intersect & ans_set
    return len(intersect)


group_sum = 0
group = []
for str in lines:
    if (len(str) > 0):
        group.append(str)
    else:
        #group_sum = group_sum + get_yes(group)
        group_sum = group_sum + get_yes_intersect(group)
        group = []

group_sum = group_sum + get_yes_intersect(group)
print(group_sum)