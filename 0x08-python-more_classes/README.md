# Python - More Classes and Objects

* **0. Simple rectangle**
  * [0-rectangle.py](./0-rectangle.py): An empty Python class that defines a rectangle.

* **1. Real definition of a rectangle**
  * [1-rectangle.py](./1-rectangle.py): A Python class that defines a rectangle. It builds on [0-rectangle.py](./0-rectangle.py) and includes the following:
    * Private instance attribute `width`.
    * Property getter `def width(self):` to get the value of `width`.
    * Property setter `def width(self, value):` to set the value of `width`.
    * Private instance attribute `height`.
    * Property getter `def height(self):` to get the value of `height`.
    * Property setter `def height(self, value):` to set the value of `height`.
    * Instantiation with optional `width` and `height`: `def __init(self, width=0, height=0):`
  * If either `width` or `height` is not an integer, a `TypeError` is raised with the message `width must be an integer` or `height must be an integer`.
  * If either `width` or `height` is less than `0`, a `ValueError` is raised with the message `width must be >= 0` or `height must be >= 0`.

* **2. Area and Perimeter**
  * [2-rectangle.py](./2-rectangle.py): A Python class that defines a rectangle. It builds on [1-rectangle.py](./1-rectangle.py) and includes the following:
    * Public instance method `def area(self):` that returns the area of the rectangle.
    * Public instance attribute `def perimeter(self):` that returns the perimeter of the rectangle. If either `width` or `height` equals `0`, the perimeter is `0`.

* **3. String representation**
  * [3-rectangle.py](./3-rectangle.py): A Python class that defines a rectangle. It builds on [2-rectangle.py](./2-rectangle.py) and includes the following:
    * Special method `__str__` to print the rectangle with the `#` character. If either `width` or `height` equals `0`, the method returns an empty string.

* **4. Eval is magic**
  * [4-rectangle.py](./4-rectangle.py): A Python class that defines a rectangle. It builds on [3-rectangle.py](./3-rectangle.py) and includes the following:
    * Special method `__repr__` to return a string representation of the rectangle.

* **5. Detect instance deletion**
  * [5-rectangle.py](./5-rectangle.py): A Python class that defines a rectangle. It builds on [4-rectangle.py](./4-rectangle.py) and includes the following:
    * Special method `__del__` that prints the message `Bye rectangle...` when a `Rectangle` instance is deleted.

* **6. How many instances**
  * [6-rectangle.py](./6-rectangle.py): A Python class that defines a rectangle. It builds on [5-rectangle.py](./5-rectangle.py) and includes the following:
    * Public class