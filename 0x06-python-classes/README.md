# Square Class

## Description

This repository contains a Python class called `Square` that defines a square and provides various functionalities related to the square.

## Contents

- [0. My first square](#0-my-first-square)
- [1. Square with size](#1-square-with-size)
- [2. Size validation](#2-size-validation)
- [3. Area of a square](#3-area-of-a-square)
- [4. Access and update private attribute](#4-access-and-update-private-attribute)
- [5. Printing a square](#5-printing-a-square)
- [6. Coordinates of a square](#6-coordinates-of-a-square)

---

## 0. My first square

- Write an empty class `Square` that defines a square.
- You are not allowed to import any module.

---

## 1. Square with size

- Write a class `Square` that defines a square by:
  - Private instance attribute: `size`
  - Instantiation with size (no type/value verification)
- You are not allowed to import any module.

---

## 2. Size validation

- Write a class `Square` that defines a square by:
  - Private instance attribute: `size`
  - Instantiation with optional size: `def __init__(self, size=0):`
  - `size` must be an integer, otherwise raise a `TypeError` exception with the message "size must be an integer".
  - If `size` is less than 0, raise a `ValueError` exception with the message "size must be >= 0".
- You are not allowed to import any module.

---

## 3. Area of a square

- Write a class `Square` that defines a square by:
  - Private instance attribute: `size`
  - Instantiation with optional size: `def __init__(self, size=0):`
  - `size` must be an integer, otherwise raise a `TypeError` exception with the message "size must be an integer".
  - If `size` is less than 0, raise a `ValueError` exception with the message "size must be >= 0".
  - Public instance method: `def area(self):` that returns the current square area.
- You are not allowed to import any module.

---

## 4. Access and update private attribute

- Write a class `Square` that defines a square by:
  - Private instance attribute: `size`
    - Property `def size(self):` to retrieve it
    - Property setter `def size(self, value):` to set it:
      - `size` must be an integer, otherwise raise a `TypeError` exception with the message "size must be an integer".
      - If `size` is less than 0, raise a `ValueError` exception with the message "size must be >= 0".
  - Instantiation with optional size: `def __init__(self, size=0):`
  - Public instance method: `def area(self):` that returns the current square area.
- You are not allowed to import any module.

---

## 5. Printing a square

- Write a class `Square` that defines a square by:
  - Private instance attribute: `size`
    - Property `def size(self):` to retrieve it
    - Property setter `def size(self, value):` to set it:
      - `size` must be an integer, otherwise raise a `TypeError` exception with the message "size must be an integer".
      - If `size` is less than 0, raise a `ValueError` exception with the message "size must be >= 0".
  -

 Instantiation with optional size: `def __init__(self, size=0):`
  - Public instance method: `def area(self):` that returns the current square area.
  - Public instance method: `def my_print(self):` that prints in stdout the square with the character '#':
    - If `size` is equal to 0, print an empty line.
- You are not allowed to import any module.

---

## 6. Coordinates of a square

- Write a class `Square` that defines a square by:
  - Private instance attribute: `size`
    - Property `def size(self):` to retrieve it
    - Property setter `def size(self, value):` to set it:
      - `size` must be an integer, otherwise raise a `TypeError` exception with the message "size must be an integer".
      - If `size` is less than 0, raise a `ValueError` exception with the message "size must be >= 0".
  - Private instance attribute: `position`
    - Property `def position(self):` to retrieve it
    - Property setter `def position(self, value):` to set it:
      - `position` must be a tuple of 2 positive integers, otherwise raise a `TypeError` exception with the message "position must be a tuple of 2 positive integers".
  - Instantiation with optional size and optional position: `def __init__(self, size=0, position=(0, 0)):`
  - Public instance method: `def area(self):` that returns the current square area.
  - Public instance method: `def my_print(self):` that prints in stdout the square with the character '#':
    - If `size` is equal to 0, print an empty line.
    - `position` should be used by using space - Don’t fill lines by spaces when `position[1] > 0`.
- You are not allowed to import any module.

---

