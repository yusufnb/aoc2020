import numpy as np
import re

with open('./day18-input.txt') as f:
    lines = f.read().splitlines()

parens = {}

# no bracket expression, evenly spaced
def eval_expression(s):
    tokens = s.split(" ")
    ans = tokens.pop(0)
    while len(tokens) > 0:
        op = tokens.pop(0)
        rs = tokens.pop(0)
        if (op == "+"):
            ans = ans + rs
        elif (op == "*"):
            ans = ans * rs
    return ans

def compact(s):
    m = re.split("(\([^\(\)]+\))", s)
    for (i, part) in enumerate(m):
        is_paren = re.match("^\(([^\(\)]+)\)$", part)
        if is_paren is not None:
            m[i] = eval_expression(is_paren.group(1))


    while m is not None:

