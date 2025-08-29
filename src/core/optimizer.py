"""Budget optimisation using a simple knapsack solver."""

from __future__ import annotations

from typing import List


def solve_knapsack(costs: List[int], benefits: List[int], budget: int) -> List[int]:
    n = len(costs)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for b in range(budget + 1):
            dp[i][b] = dp[i - 1][b]
            c = costs[i - 1]
            if c <= b:
                dp[i][b] = max(dp[i][b], dp[i - 1][b - c] + benefits[i - 1])
    res = [0] * n
    b = budget
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            res[i - 1] = 1
            b -= costs[i - 1]
    return res
