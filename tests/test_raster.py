import pytest

from render import raster as mod

CASES = [
    ('bresenham', [0, 0, 2, 0], [[0, 0], [1, 0], [2, 0]], False),
    ('bresenham', [0, 0, 0, 0], [[0, 0]], False),
    ('clip_line', [0, 0, 10, 0, [2, -1, 5, 1]], [[2, 0.0], [5, 0.0]], False),
    ('clip_line', [-5, 0, -1, 0, [0, 0, 4, 4]], None, False),
    ('midpoint_circle', [0, 0, 1], [[-1, 0], [0, -1], [0, 1], [1, 0]], False),
    ('rect_contains', [[0, 0, 2, 2], [0, 0]], True, False),
    ('rect_contains', [[0, 0, 2, 2], [3, 3]], False, False),
    ('fill_span', [1, 0, 2], [[0, 1], [1, 1], [2, 1]], False),
    ('bresenham', [0, 0, 2, 1], [[0, 0], [1, 1], [2, 1]], False),
    ('clip_line', [0, 0, 1, 1, [0, 0, 2, 2]], [[0, 0], [1, 1]], False),
    ('midpoint_circle', [1, 1, 0], [[1, 1]], False),
    ('rect_contains', [[0, 0, 0, 0], [0, 0]], True, False),
    ('fill_span', [0, 1, 1], [[1, 0]], False),
    ('clip_line', [0, 0, 0, 10, [0, 0, 0, 0]], [[0, 0], [0.0, 0]], False),
    ('bresenham', [2, 2, 0, 0], [[2, 2], [1, 1], [0, 0]], False),
]


@pytest.mark.parametrize("func_name,args,expected,approx", CASES)
def test_raster_contract(func_name, args, expected, approx):
    func = getattr(mod, func_name)
    result = func(*args)
    if approx:
        assert result == pytest.approx(expected)
    else:
        assert result == expected
