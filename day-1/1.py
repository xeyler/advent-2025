dial_pos = 50
password = 0

with open('input') as f:
    for line in f:
        line = line.rstrip()
        movement = int(line[1:])
        movement = movement * (-1 if line[0] == "L" else 1)
        dial_pos = (dial_pos + movement) % 100
        if dial_pos == 0:
            password = password + 1

print(password)
