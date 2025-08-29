from src.core.multicriteria import total_score


def test_total_score():
    items = [
        {
            "score_state": 80,
            "score_traffic": 90,
            "score_safety": 70,
            "score_bcr": 60,
            "score_co2": 50,
        },
        {
            "score_state": 60,
            "score_traffic": 50,
            "score_safety": 70,
            "score_bcr": 60,
            "score_co2": 50,
        },
    ]
    weights = {"state": 0.4, "traffic": 0.2, "safety": 0.2, "bcr": 0.1, "co2": 0.1}
    res = total_score(items, weights)
    assert res[0] > res[1]
