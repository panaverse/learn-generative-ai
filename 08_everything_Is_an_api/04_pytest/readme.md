# Testing Python

[pytest](https://docs.pytest.org/en/7.4.x/getting-started.html#getstarted)

Run the following command in root directory:

    pytest


pytest will run all files of the form test_*.py or *_test.py in the current directory and its subdirectories. 

 **Test-Driven Development (TDD)**

**TDD is a software development approach where you write tests before writing the actual code.** It follows a cyclical process called the "Red-Green-Refactor" cycle:

1. **Red:**
   - Write a failing test that describes a desired feature or behavior.
   - Run the test to ensure it fails (red state).

2. **Green:**
   - Write the minimal amount of code to make the test pass (green state).
   - Resist the urge to write more code than necessary.

3. **Refactor:**
   - Improve the code's design and readability without changing its functionality.
   - Ensure all tests still pass after refactoring.

**Here's an illustrative example in Python using pytest:**

**1. Red:**

```python
# tests/test_calculator.py
import pytest

def test_add():
    result = calculator.add(2, 3)  # Calculator class doesn't exist yet
    assert result == 5
```

**2. Green:**

```python
# calculator.py
class Calculator:
    def add(self, a, b):
        return a + b
```

**3. Refactor:**

```python
# calculator.py (refactored)
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, value):
        self.result += value

    def get_result(self):
        return self.result
```

**Key benefits of TDD:**

- **Higher-quality code:** Focused on requirements and tested from the start.
- **Improved design:** Code evolves through small, testable steps.
- **Early defect detection:** Catches problems early, reducing debugging time.
- **Documentation:** Tests serve as a form of living documentation.
- **Confidence in changes:** Refactoring without fear of breaking functionality.

**Remember:**

- TDD is a discipline that takes practice to master.
- It may feel counterintuitive at first, but the benefits are worth it.
- Start with small, manageable tests and work incrementally.
- Use a testing framework like pytest for efficient test execution.
- Embrace refactoring as an essential part of the process.
