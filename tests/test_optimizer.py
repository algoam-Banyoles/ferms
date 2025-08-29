from src.core.optimizer import solve_knapsack


def test_knapsack():
    costs = [40, 60, 30]
    benefits = [40, 90, 50]
    sel = solve_knapsack(costs, benefits, budget=90)
    assert sum(sel) >= 2
    assert sel[1] == 1
