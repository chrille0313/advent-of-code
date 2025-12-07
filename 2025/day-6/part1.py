def convert_to_columns(rows):
    num_columns = len(rows[0])
    return [[row[c] for row in rows] for c in range(num_columns)]


with open("input.txt") as f:
    rows = [line.strip().split() for line in f if line.strip()]

problems = convert_to_columns(rows)
results = [eval(terms[-1].join(terms[:-1])) for terms in problems]
print(sum(results))
