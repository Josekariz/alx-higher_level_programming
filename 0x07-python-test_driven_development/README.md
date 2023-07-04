# Python - Test-driven development

This project focuses on test-driven development in Python, utilizing `docstring` and `unittest`.

## Tests ✅

* [tests](./tests): This folder contains both provided test files and the following eight independently-developed tests:
  * [0-add_integer.txt](./tests/0-add_integer.txt)
  * [2-matrix_divided.txt](./tests/2-matrix_divided.txt)
  * [3-say_my_name.txt](./tests/3-say_my_name.txt)
  * [4-print_square.txt](./tests/4-print_square.txt)
  * [5-text_indentation.txt](./tests/text_indentation.txt)
  * [6-max_integer_test.py](./tests/6-max_integer_test.py)
  * [100-matrix_mul.txt](./tests/100-matrix_mul.txt)
  * [101-lazy_matrix_mul.txt](./tests/101-lazy_matrix_mul.txt)

## Function Prototypes 💾

Here are the prototypes for the functions implemented in this project:

| File                     | Prototype                                    |
| ------------------------ | -------------------------------------------- |
| `0-add_integer.py`       | `def add_integer(a, b=98):`                  |
| `2-matrix_divided.py`    | `def matrix_divided(matrix, div):`           |
| `3-say_my_name.py`       | `def say_my_name(first_name, last_name=""):` |
| `4-print_square.py`      | `def print_square(size):`                    |
| `5-text_indentation.py`  | `def text_indentation(text):`                |
| `100-matrix_mul.py`      | `def matrix_mul(m_a, m_b):`                  |
| `101-lazy_matrix_mul.py` | `def lazy_matrix_mul(m_a, m_b):`             |
| `102-python.c`           | `void print_python_string(PyObject *p);`     |

## Tasks 📃

* **0. Integers addition**
  * [0-add_integer.py](./0-add_integer.py): This Python function returns the integer addition of two numbers.
  * If either `a` or `b` is not an `int` or `float`, a `TypeError` is raised with the message `a must be an integer` or `b must be an integer`.
  * If either `a` or `b` is a `float`, it is casted to an `int` before performing the addition.

* **1. Divide a matrix**
  * [2-matrix_divided.py](./2-matrix_divided.py): This Python function divides all elements of a matrix by a common divisor.
  * It returns a new matrix representing the division of all elements of `matrix` by `div`.
  * Quotients are rounded to two decimal places.
  * If `matrix` is not a list of lists of `int`s or `float`s, a `TypeError` is raised with the message `matrix must be a matrix (list of lists) of integers/floats`.
  * If `matrix` contains rows of different lengths, a `TypeError` is raised with the message `Each row of the matrix must have the same size`.
  * If the divisor `div` is not an `int` or `float`, a `TypeError` is raised with the message `div must be a number`.
  * If `div` is `0`, a `ZeroDivisionError` is raised with the message `division by zero`.

* **2. Say my name**
  * [3-say_my_name.py](./3-say_my_name.py): This Python function prints

 a name in the format `My name is <first_name> <last_name>`.
  * If either `first_name` or `last_name` is not a `str`, a `TypeError` is raised with the message `first_name must be a string` or `last_name must be a string`.

* **3. Print square**
  * [4-print_square.py](./4-print_square.py): This Python function prints a square using the `#` character.
  * The parameter `size` represents the height/width of the square.
  * If `size` is not an `int`, a `TypeError` is raised with the message `size must be an integer`.
  * If `size` is less than `0`, a `ValueError` is raised with the message `size must be >= 0`.

* **4. Text indentation**
  * [5-text_indentation.py](./5-text_indentation.py): This Python function prints text with indentation.
  * Two new lines are printed after any `.`, `?`, or `:` character.
  * If `text` is not a `str`, a `TypeError` is raised with the message `text must be a string`.
  * No spaces are printed at the beginning or end of each printed line.

* **5. Max integer - Unittest**
  * [tests/6-max_integer_test.py](./tests/6-max_integer_text.py): This Python class/script contains unittests for the function `def max_integer(list=[]):` (provided by  School).

* **6. Matrix multiplication**
  * [100-matrix_mul.py](./100-matrix_mul.py): This Python function multiplies two matrices.
  * It returns a new matrix representing the multiplication of `m_a` by `m_b`.
  * If either `m_a` or `m_b` is empty (i.e., `== []` or `== [[]]`), a `ValueError` is raised with the message `m_a can't be empty` or `m_b can't be empty`.
  * If either `m_a` or `m_b` is not a list, a `TypeError` is raised with the message `m_a must be a list` or `m_b must be a list`.
  * If either `m_a` or `m_b` is not a list of lists, a `TypeError` is raised with the message `m_a must be a list of lists` or `m_b must be a list of lists`.
  * If either `m_a` or `m_b` is not a list of lists of `int`s or `float`s, a `TypeError` is raised with the message `m_a should contain only integers or floats` or `m_b should contain only integers or floats`.
  * If either `m_a` or `m_b` contains rows of different lengths, a `TypeError` is raised with the message `each row of m_a must should be of the same size` or `each row of m_b must should be of the same size`.
  * If `m_a` and `m_b` cannot be multiplied (i.e., the row size of `m_a` does not match the column size of `m_b`), a `ValueError` is raised with the message `m_a and m_b can't be multiplied`.

* **7. Lazy matrix multiplication**
  * [101-lazy_matrix_mul.py](./101-lazy_matrix_mul.py): This Python function multiplies two matrices using the NumPy module.
  * It has the same functionality as [100-matrix_mul.py](./100-matrix_mul.py).

* **8. CPython #3:

 Python Strings**
  * [102-python.c](./102-python.c): This C function prints basic information about Python string objects.