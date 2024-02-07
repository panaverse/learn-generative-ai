# Python Docstrings

[Python Docstrings Details](https://www.programiz.com/python-programming/docstrings)

 **Python Docstrings** are a special kind of comment used to document Python modules, functions, classes, and methods. They provide a concise and informative way to explain the purpose, usage, and behavior of your code.

**Here's how to write Docstrings:**

1. **Position:** Place Docstrings immediately after the definition of the function, class, or method they describe.
2. **Enclose in Triple Quotes:** Enclose Docstrings within triple quotes (either single or double) to allow for multi-line descriptions.
3. **First Line (Summary):** Begin the Docstring with a concise and informative summary of the object's purpose.
4. **Optional Additional Lines:** If needed, provide more detailed descriptions, usage examples, parameter explanations, return values, or other relevant information in subsequent lines.

**Example:**

```python
def greet(name:str)->str:
    """Greets the user by name.

    Args:
        name (str): The name of the person to greet.

    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"
```

**Key Points:**

- Docstrings are accessible using the `__doc__` attribute of the object.
- They can be displayed using the `help()` function in interactive Python sessions.
- Popular tools like Sphinx and PyCharm utilize Docstrings to generate comprehensive documentation.

**Common Docstring Formats:**

- **Google style:** Emphasizes readability and consistency.
- **NumPy/SciPy style:** Focuses on technical documentation for scientific computing.
- **reStructuredText:** Offers advanced formatting for complex documentation.

**Writing Effective Docstrings:**

- Keep Docstrings clear and concise, avoiding unnecessary verbosity.
- Use plain English and avoid jargon.
- Provide practical examples to illustrate usage.
- Update Docstrings as code evolves.
- Follow a consistent style guide for readability and maintainability.

**Benefits of Docstrings:**

- Enhance code readability and maintainability.
- Facilitate collaboration and code sharing.
- Enable self-documenting code.
- Generate comprehensive documentation for users and developers.
- Serve as a guide for interactive help systems.

By embracing Docstrings, you can create well-documented, informative, and user-friendly Python code that's easier to understand, maintain, and share with others.

