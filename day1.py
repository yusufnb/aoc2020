from bisect import bisect_left

# https://stackoverflow.com/a/49281681
def find_elem_in_sorted_list(elem, sorted_list):
    # https://docs.python.org/3/library/bisect.html
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(sorted_list, elem)
    if i != len(sorted_list) and sorted_list[i] == elem:
        return i
    return -1

with open('./day1-input.txt') as f:
    lines = f.read().splitlines()
lines = [int(i) for i in lines]
lines.sort()

def find_product(sum, sorted_list):
    for i in sorted_list:
        x = sum - i
        if (find_elem_in_sorted_list(sum - i, sorted_list) != -1):
            return (x*i)
    return -1;

for i in lines:
    x = 2020 - i
    prod = find_product(x, lines)
    if (prod > 0):
        print (prod * i)
        break
