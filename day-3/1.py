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
    tens = max(bank[:-1])
    tens_place = bank.index(tens)
    ones = max(bank[tens_place + 1:])
    result = result + tens * 10 + ones

print(result)
