import pytest
from easy import isbn

def test_isbn():
    assert isbn.last_digit('978-0-306-40615') == '978-0-306-40615-7'