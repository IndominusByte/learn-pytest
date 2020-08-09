import pytest

@pytest.mark.parametrize("test_input", [("3+5", 8), ("2+4", 6), ("6*9", 54)])
def test_eval(test_input):
    value, result = test_input
    assert eval(value) == result
