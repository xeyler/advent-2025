import math
import re

banks = list()

with open("input") as f:
    for line in f:
        bank = list()
        for char in line:
            if char == "\n":
                continue
            bank.append(int(char))
        banks.append(bank)

result = 0

for bank in banks:
    bank_len = len(bank)
    for i in range(-11, 1):
        n = max(bank[:i] if i else bank)
        n_place = bank.index(n)
        bank = bank[n_place + 1:]
        result = result + n * 10 ** abs(i)

print(result)
