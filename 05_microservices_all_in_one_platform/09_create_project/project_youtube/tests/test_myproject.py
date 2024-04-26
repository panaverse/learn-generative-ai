from project_youtube import main

def test_function1():
    r = main.my_first_function()
    assert r == "Hello World"

def test_function2():
    r = main.my_first_function()
    assert r != "Pakistan"