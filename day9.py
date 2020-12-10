import re
import bisect

with open('./day9-input.txt') as f:
    lines = f.read().splitlines()

lines = [int(i) for i in lines]

pre_len = 25

def find_elem_in_sorted_list(elem, sorted_list):
    # https://docs.python.org/3/library/bisect.html
    'Locate the leftmost value exactly equal to x'
    i = bisect.bisect_left(sorted_list, elem)
    if i != len(sorted_list) and sorted_list[i] == elem:
        return i
    return -1

def insert_in_sorted_list(elem, sorted_list):
    bisect.insort(sorted_list, elem)
    sorted_list

def is_valid(elem, sorted_list):
    for e in sorted_list:
        if e > elem or elem - e < e :
            return False
        diff = elem - e
        ind = find_elem_in_sorted_list(diff, sorted_list)
        if (ind >= 0):
            return True
    return False

def part1():
    global pre_len
    global lines
    pre_list = lines[0:pre_len]
    pre_list = sorted(pre_list)
    for i in range(pre_len, len(lines)):
        if not is_valid(lines[i], pre_list):
            return(lines[i])
            break
        else:
            ind = find_elem_in_sorted_list(lines[i-pre_len], pre_list)
            del pre_list[ind]
            pre = insert_in_sorted_list(lines[i], pre_list)

def part2():
    num = part1()
    print(num)
    ptr = 0
    while(ptr < len(lines)):
        sum = lines[ptr]
        for i in range(ptr+1, len(lines)):
            sum = sum + lines[i]
            if (sum == num):
                ans_list = sorted(lines[ptr:(i+1)])
                return ans_list[0] + ans_list[len(ans_list) - 1]
            if (sum > num):
                break
        ptr = ptr + 1


print(part2())

