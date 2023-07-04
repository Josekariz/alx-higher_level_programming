Here are the answers to the questions in the "Everything is object" project:

* **0. Who am I?**
  * `type()` function is used to print the type of an object.
  * Answer: `type()`

* **1. Where are you?**
  * `id()` function is used to get a variable's identifier (memory address).
  * Answer: `id()`

* **2. Right count**
  * In the given code, `a` and `b` do not point to the same object.
  * Answer: No

* **3. Right count =**
  * In the given code, `a` and `b` point to the same object.
  * Answer: Yes

* **4. Right count =**
  * In the given code, `a` and `b` point to the same object.
  * Answer: Yes

* **5. Right count =+**
  * In the given code, `a` and `b` do not point to the same object.
  * Answer: No

* **6. Is equal**
  * The three lines print `True` because `s1` and `s2` have the same value.
  * Answer: True

* **7. Is the same**
  * The three lines print `True` because `s1` and `s2` point to the same object.
  * Answer: True

* **8. Is really equal**
  * The three lines print `True` because `s1` and `s2` have the same value.
  * Answer: True

* **9. Is really the same**
  * The three lines print `True` because `s1` and `s2` point to the same object.
  * Answer: True

* **10. And with a list, is it equal**
  * The three lines print `True` because `l1` and `l2` have the same value.
  * Answer: True

* **11. And with a list, is it the same**
  * The three lines print `False` because `l1` and `l2` do not point to the same object.
  * Answer: False

* **12. And with a list, is it really equal**
  * The three lines print `True` because `l1` and `l2` have the same value.
  * Answer: True

* **13. And with a list, is it really the same**
  * The three lines print `True` because `l1` and `l2` point to the same object.
  * Answer: True

* **14. List append**
  * The script prints `[1, 2, 3, 4]` because `l1` and `l2` point to the same list object, and appending an element to `l1` modifies the list.
  * Answer: `[1, 2, 3, 4]`

* **15. List add**
  * The script prints `[1, 2, 3]` because the line `l1 = l1 + [4]` creates a new list object and assigns it to `l1`, while `l2` still points to the original list.
  * Answer: `[1, 2, 3]`

* **16. Integer incrementation**
  * The script prints `1` because the `increment` function operates on a local copy of the `a` variable, and modifying the local copy doesn't affect the original variable.
  * Answer: `1`

Here are the answers to the questions in the "Everything is object" project:

* **17. List incrementation**
  * The script prints `[1, 2, 3, 4]` because the `increment` function appends the value `4` to the list `n`, which is the same list object as `l`.
  * Answer: `[1, 2, 3, 4]`

* **18. List assignation**
  * The script prints `[1, 2, 3]` because the `assign_value` function assigns the value of `v` to the local variable `n`, but it doesn't modify the original list `l1`.
  * Answer: `[1, 2, 3]`

* **19. Copy a list object**
  * [19-copy_list.py](./19-copy_list.py) contains a Python function `def copy_list(l):` that returns a copy of a list.
  * Answer: [19-copy_list.py](./19-copy_list.py)

* **20. Tuple or not?**
  * [20-answer.txt](./20-answer.txt): `a` is not a tuple. It is an empty tuple.
  * Answer: [20-answer.txt](./20-answer.txt)

* **21. Tuple or not?**
  * [21-answer.txt](./21-answer.txt): `a` is a tuple.
  * Answer: [21-answer.txt](./21-answer.txt)

* **22. Tuple or not?**
  * [22-answer.txt](./22-answer.txt): `a` is not a tuple. It is an integer.
  * Answer: [22-answer.txt](./22-answer.txt)

* **23. Tuple or not?**
  * [23-answer.txt](./23-answer.txt): `a` is a tuple.
  * Answer: [23-answer.txt](./23-answer.txt)

* **24. Who I am?**
  * [24-answer.txt](./24-answer.txt): The script prints `False` because `a` and `b` are two different tuple objects with the same value.
  * Answer: [24-answer.txt](./24-answer.txt)

* **25. Tuple or not**
  * [25-answer.txt](./25-answer.txt): The script prints `False` because `a` and `b` are two different tuple objects with the same value.
  * Answer: [25-answer.txt](./25-answer.txt)

* **26. Empty is not empty**
  * [26-answer.txt](./26-answer.txt): The script prints `True` because `a` and `b` are two empty tuple objects, and empty tuples are immutable and interned in Python.
  * Answer: [26-answer.txt](./26-answer.txt)

* **27. Still the same**
  * [27-answer.txt](./27-answer.txt): The last line of the script will print a different memory address (object identifier) than the first line because the line `a = a + [5]` creates a new list object, which is assigned to `a`.
  * Answer: [27-answer.txt](./27-answer.txt)

* **28. Same or not?**
  * [28-answer.txt](./28-answer.txt): The last line of the script will print the same memory address (object identifier) as the first line because the `+=` operator modifies the list in-place, keeping the same object.
  * Answer: [28-answer.txt](./28-answer.txt)

* **29. #pythonic**
  * [100-magic_string.py](./100-magic_string.py) contains a Python function `magic_string()` that returns the string
