def is_repeated_twice(s):
    if len(s) % 2 != 0:
        return False

    mid = len(s) // 2
    return s[:mid] == s[mid:]


with open("input.txt") as f:
    ranges = [[int(i) for i in r.split("-")] for r in f.read().strip().split(",")]

invalid_ids = []
for start, stop in ranges:
    for n in range(start, stop + 1):
        if is_repeated_twice(str(n)):
            invalid_ids.append(n)

print(sum(invalid_ids))
