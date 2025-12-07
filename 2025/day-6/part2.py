with open("input.txt") as f:
    lines = [line.strip("\n") for line in f.readlines()]
    problems = []

    current_problem = []
    new_problem = True

    for c in range(len(lines[0])):
        if new_problem:
            current_problem.append(lines[-1][c])
            new_problem = False

        column = [line[c] for line in lines[:-1]]
        if all(ch == ' ' for ch in column):
            problems.append(list(reversed(current_problem)))
            current_problem = []
            new_problem = True
            continue

        current_problem.append(''.join(column).replace(' ', ''))

    problems.append(list(reversed(current_problem)))

results = [eval(terms[-1].join(terms[:-1])) for terms in reversed(problems)]
print(sum(results))
