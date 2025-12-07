from math import inf


def dp(batteries, i, position, memo):
    if position == -1:
        return 0
    if i == len(batteries):
        return -inf

    state = (i, position)
    if state in memo:
        return memo[state]

    take = batteries[i] * (10 ** position) + dp(batteries, i + 1, position - 1, memo)
    leave = dp(batteries, i + 1, position, memo)

    memo[state] = max(take, leave)

    return memo[state]


with open("input.txt") as f:
    banks = [[int(i) for i in line.strip()] for line in f if line.strip()]

print(sum(dp(bank, 0, 11, {}) for bank in banks))
