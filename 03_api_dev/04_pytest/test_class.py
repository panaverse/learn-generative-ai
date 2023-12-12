# Group multiple tests in a class

# Once you develop multiple tests, you may want to group
# them into a class. pytest makes it easy to create a class
# containing more than one test:

# content of test_class.py
class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")

# pytest discovers all tests following its Conventions for 
# Python test discovery, so it finds both test_ prefixed 
# functions. There is no need to subclass anything, but 
# make sure to prefix your class with Test otherwise the 
# class will be skipped. We can simply run the module by 
# passing its filename.

#   pytest -q test_class.py

# Something to be aware of when grouping tests inside 
# classes is that each test has a unique instance of the 
# class. Having each test share the same class instance 
# would be very detrimental to test isolation and would 
# promote poor test practices. 

