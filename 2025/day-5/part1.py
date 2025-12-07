def merge_ranges(ranges):
    merged = []

    for start, end in sorted(ranges):
        if not merged or merged[-1][1] < start:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    return merged


def in_ranges(value, ranges):
    return any(start <= value <= end for start, end in ranges)


with open("input.txt") as f:
    ranges = []
    ingredients = []

    for line in f.readlines():
        if "-" in line:
            ranges.append(sorted(int(x) for x in line.strip().split("-")))
        elif line.strip():
            ingredients.append(int(line.strip()))

ranges = merge_ranges(ranges)
print(sum(in_ranges(ingredient, ranges) for ingredient in ingredients))
