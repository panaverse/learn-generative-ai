# content of test_sysexit.py
import pytest


def f()-> None:
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()