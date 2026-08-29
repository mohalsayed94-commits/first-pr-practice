from greet import greet


def test_greet_returns_expected_message():
    assert greet("World") == "Hello, World!"


def test_greet_uses_given_name():
    assert greet("Alice") == "Hello, Alice!"
