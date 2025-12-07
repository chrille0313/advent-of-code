with open("input.txt") as f:
    lines = [line.strip() for line in f if line.strip()]

dial = 50
total = 0

for line in lines:
    direction = 1 if line[0] == "R" else -1
    steps = int(line[1:])

    revolutions = steps // 100
    steps -= revolutions * 100

    new_dial = dial + steps * direction
    passed_zero = dial != 0 and (new_dial <= 0 or 100 <= new_dial)

    total += revolutions + passed_zero
    dial = new_dial % 100

print(total)
