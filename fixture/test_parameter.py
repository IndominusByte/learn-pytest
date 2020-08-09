import pytest

@pytest.mark.parametrize("username",['oman','okky','paulus'])
def test_param(username):
    assert username in ['oman','okky','paulus']
