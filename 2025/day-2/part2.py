def is_repeated_at_least_twice(s):
    return s in (s + s)[1:-1]


with open("input.txt") as f:
    ranges = [[int(i) for i in r.split("-")] for r in f.read().strip().split(",")]

invalid_ids = []
for start, stop in ranges:
    for n in range(start, stop + 1):
        if is_repeated_at_least_twice(str(n)):
            invalid_ids.append(n)

print(sum(invalid_ids))
