from simple.print_hello import print_hello

def test_hello(capsys):
    """Test that checks if print_hello prints hello"""

    print_hello()
    captured = capsys.readouterr()
    assert captured.out == "hello\n"