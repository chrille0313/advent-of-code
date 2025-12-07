with open("input.txt") as f:
    lines = [line.strip() for line in f if line.strip()]

dial = 50
total = 0

for line in lines:
    direction = 1 if line[0] == "R" else -1
    steps = int(line[1:])

    dial = (dial + steps * direction) % 100
    total += dial == 0

print(total)
