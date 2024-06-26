import simple


def test_hello(capsys):
    """Test that checks if print_hello prints hello"""

    simple.print_hello()
    captured = capsys.readouterr()
    assert captured.out == "hello\n"
