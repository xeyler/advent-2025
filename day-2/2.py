import math
import re

from textwrap import wrap

ranges = set()
invalid_ids = set()

with open("input") as f:
    for line in f:
        rangestrings = re.findall(r"([0-9]+)\-([0-9]+),?", line)
        for left, right in rangestrings:
            left = int(left)
            right = int(right)
            assert(left <= right)
            ranges.add((left, right))

def cut_into_n_sections(i, n):
    i = str(i)
    i = wrap(i, width=n)
    i = [int(x) for x in i]
    return i

def is_symmetric(i):
    num_digits = int(math.log10(i)) + 1
    n = 0
    while n < num_digits / 2:
        n = n + 1
        if num_digits % n:
            continue

        sections = cut_into_n_sections(i, n)

        if sections.count(sections[0]) == len(sections) and len(sections) > 1:
            return True
    return False

for left, right in ranges:
    i = left
    while i <= right:
        if is_symmetric(i):
            invalid_ids.add(i)
        i = i + 1

sum = 0
for invalid_id in invalid_ids:
    sum = sum + invalid_id
print(sum)

