from calculator import add


def test_add():
    # BDD
    # Given
    a = 5
    b = 6
    # When
    result = add(a, b)
    # Then
    assert result == 11


def test_add_simple():
    assert add(5, 6) == 11
