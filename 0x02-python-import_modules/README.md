# 0x02. Python - import & modules

This readme provides a brief description of the tasks and requirements for each program in the Toolbox project.

## 1. My first toolbox!

Write a program that imports functions from the file `calculator_1.py`, performs some mathematical operations, and prints the results.

**Requirements:**
- Use the function `print` (with string format to display integers) no more than 4 times.
- Define the value 10 to a variable called `a` and the value 5 to a variable called `b`.
- Use the variables `a` and `b` as arguments when calling the imported functions (including `print`).
- Each variable (`a` and `b`) must be defined in a separate line (`a = 10` and another line for `b = 5`).
- The program should call each of the imported functions and print the results.

## 2. How to make a script dynamic!

Write a program that prints the number of arguments and the list of its arguments.

**Requirements:**
- The output should display the number of arguments, followed by "argument" if there is only one argument, or "arguments" if there are multiple arguments.
- If there is at least one argument, the output should include a colon ":" after the word "arguments". Otherwise, it should end with a period ".".
- The program should print each argument on a separate line, including the argument's position (starting at 1), a colon ":", the argument value, and a new line.
- The code should not be executed when imported.

## 3. Infinite addition

Write a program that prints the result of adding all the arguments together.

**Requirements:**
- The output should display the result of the addition of all arguments, followed by a new line.
- Arguments should be cast into integers using the `int()` function. Assume that all arguments can be casted into integers.
- The code should not be executed when imported.

## 4. Who are you?

Write a program that prints all the names defined by the compiled module `hidden_4.pyc`.

**Requirements:**
- The program should print one name per line, in alphabetical order.
- Only names that do not start with "__" should be printed.
- The code should not be executed when imported.

## 5. Everything can be imported

Write a program that imports the variable `a` from the file `variable_load_5.py` and prints its value.

**Requirements:**
- Do not use "*" for importing or the `__import__` function.
- The code should not be executed when imported.

Please refer to each individual program for more detailed explanations and implementation instructions.