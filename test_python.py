import math


def test_pi():
    assert round(math.pi, 1) == 3.1


def test_sqrt():
    assert math.sqrt(4) == 2
    assert math.sqrt(9) == 3
    assert math.sqrt(4)**2 == 4


def test_pow():
    assert math.pow(2, 2) == 4
    assert math.pow(3, 3) == 27
    assert math.pow(2, 3) == 8


def test_hypotenuse():
    assert math.hypot(2, 3) == math.sqrt(2*2 + 3*3)


def test_filter():
    numbers = [-1, -5, 4, 2]
    assert list(filter(lambda x: (x > 0), numbers)) == [4, 2]
    assert list(filter(lambda x: (x < 0), numbers)) == [-1, -5]
    assert list(filter(lambda x: (x % 2 == 0), numbers)) == [4, 2]


def test_map():
    numbers = [-1, -5, 4, 2]
    assert list(map(lambda x: (x * 2), numbers)) == [-2, -10, 8, 4]


def test_sorted():
    numbers = [-1, -5, 4, 2]
    assert sorted(numbers) == [-5, -1, 2, 4]
    assert sorted(numbers, reverse=True) == [4, 2, -1, -5]
