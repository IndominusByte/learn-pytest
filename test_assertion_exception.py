import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def myfunc():
    raise ValueError("Exception 123 raised")

def test_match():
    with pytest.raises(ValueError, match=r".* 123 .*"):
        myfunc()

@pytest.mark.xfail(raises=ZeroDivisionError)
def test_f():
    """
    @pytest.mark.xfail with a check function is probably better
    for something like documenting unfixed bugs
    (where the test describes what “should” happen) or bugs in dependencies.
    """
    1 / 0
