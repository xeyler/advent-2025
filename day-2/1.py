import math
import re

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

def is_symmetric(i):
    num_digits = int(math.log10(i)) + 1
    if num_digits % 2:
        return False

    upper_half = int(i // (10 ** (num_digits / 2)))
    lower_half = int(i % (10 ** (num_digits / 2)))
    return upper_half == lower_half

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

