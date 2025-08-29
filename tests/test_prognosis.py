from src.core.prognosis import Gompertz, LinearPiecewise


def test_linear_piecewise():
    model = LinearPiecewise(y0=1, k1=1, k2=2, switch=2)
    years = [0, 1, 2, 3, 4]
    assert model.predict(years) == [1, 2, 3, 5, 7]


def test_gompertz():
    model = Gompertz(a=1, b=1, c=1)
    val0 = model.predict([0])[0]
    assert 0.36 < val0 < 0.37
