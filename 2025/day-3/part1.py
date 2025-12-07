
with open("input.txt") as f:
    banks = [[int(i) for i in line.strip()] for line in f.readlines()]

best = []

for bank in banks:
    max_second = []

    largest = 0
    for battery in reversed(bank[1:]):
        largest = max(largest, battery)
        max_second.append(largest)

    max_second.reverse()

    largest_combination = 0

    for i, battery in enumerate(bank[:-1]):
        largest_combination = max(largest_combination, battery * 10 + max_second[i])

    best.append(largest_combination)

print(sum(best))
