import pytest

DEFAULT_CONFIG = {"user": "user1", "database": "db1"}


def create_connection_string():
    """Creates a connection string from input or defaults."""
    config = DEFAULT_CONFIG
    return f"User Id={config['user']}; Location={config['database']};"

def test_connection(monkeypatch):

    # Patch the values of DEFAULT_CONFIG to specific
    # testing values only for this test.
    monkeypatch.setitem(DEFAULT_CONFIG, "user", "test_user")
    monkeypatch.setitem(DEFAULT_CONFIG, "database", "test_db")

    # expected result based on the mocks
    expected = "User Id=test_user; Location=test_db;"

    # the test uses the monkeypatched dictionary settings
    result = create_connection_string()
    assert result == expected

def test_missing_user(monkeypatch):

    # patch the DEFAULT_CONFIG t be missing the 'user' key
    monkeypatch.delitem(DEFAULT_CONFIG, "user", raising=True)

    # Key error expected because a config is not passed, and the
    # default is now missing the 'user' entry.
    with pytest.raises(KeyError):
        create_connection_string()
