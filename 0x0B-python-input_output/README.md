# Python - Input/Output

This project focuses on file handling in Python, utilizing various input/output operations. The built-in functions `with`, `open`, and `read`, along with the `json` module, are employed for file manipulation, as well as serialization and deserialization of objects using JSON.

## Function Prototypes :floppy_disk:

Below are the function prototypes implemented in this project:

| File        | Prototype               |
| ----------- | ----------------------- |
| `0-read_file.py` | `def read_file(filename=""):` |
| `1-number_of_lines.py` | `def number_of_lines(filename=""):` |
| `2-read_lines.py` | `def read_lines(filename="", nb_lines=0):` |
| `3-write_file.py` | `def write_file(filename="", text=""):` |
| `2-append_write.py` | `def append_write(filename="", text=""):` |
| `3-to_json_string.py` | `def to_json_string(my_obj):` |
| `4-from_json_string.py` | `def from_json_string(my_str):` |
| `5-save_to_json_file.py` | `def save_to_json_file(my_obj, filename):` |
| `6-load_from_json_file.py` | `def load_from_json_file(filename):` |
| `8-class_to_json.py` | `def class_to_json(obj):` |
| `12-pascal_triangle.py` | `def pascal_triangle(n):` |
| `100-append_after.py` | `def append_after(filename="", search_string="", new_string=""):` |

## Tasks :page_with_curl:

* **0. Read file**
  * [0-read_file.py](./0-read_file.py): This Python function prints the contents of a UTF8 text file to the standard output.

* **1. Write to a file**
  * [1-write_file.py](./1-write_file.py): This Python function writes a string to a UTF8 text file and returns the number of characters written.

* **2. Append to a file**
  * [2-append_write.py](./2-append_write.py): This Python function appends a string to the end of a UTF8 text file and returns the number of characters appended.

* **3. To JSON string**
  * [3-to_json_string.py](./3-to_json_string.py): This Python function returns the JSON string representation of an object.

* **4. From JSON string to Object**
  * [4-from_json_string.py](./4-from_json_string.py): This Python function returns the Python object represented by a JSON string.

* **5. Save Object to a file**
  * [5-save_to_json_file.py](./5-save_to_json_file.py): This Python function writes an object to a text file using JSON representation.

* **6. Create object from a JSON file**
  * [6-load_from_json_file.py](./6-load_from_json_file.py): This Python function creates an object from a `.json` file.

* **7. Load, add, save**
  * [7-add_item.py](./7-add_item.py): This Python script stores all command line arguments in a Python list, which is then saved in the file `add_item.json`.

* **8. Class to JSON**
  * [8-class_to_json.py](./8-class_to_json.py): This Python function returns the dictionary description for simple Python data structures such as lists, dictionaries, strings, integers, and booleans.

* **9. Student to JSON**
  * [9-student.py](./9-student.py): This Python class `Student` defines a student and includes public instance attributes `first_name`, `last_name`, and `age`. It also provides an instantiation method `__init__(self, first_name, last_name, age)` and a public method `to_json(self)` that returns the dictionary representation of a `Student` instance.

* **10. Student to JSON with filter**
  * [10-student.py](./10-student.py): This Python class `Student` builds on [11-student.py](./11-student.py) and adds a public method `to_json(self, attrs=None)` that returns the dictionary representation of a `Student` instance. If `attrs` is a list of strings, only the listed attributes are represented in the dictionary.

* **11. Student to disk and reload**
  * [11-student.py](./11-student.py): This Python class `Student` builds on [12-student.py](./12-student.py) and includes a public method `reload_from_json(self, json)` that replaces all attributes of the `Student` instance using the key/value pairs provided in `json`. The method assumes `json` is a dictionary containing attribute names and corresponding values.

* **12. Pascal's Triangle**
  * [12-pascal_triangle.py](./12-pascal_triangle.py): This Python function returns a list of lists of integers representing Pascal's triangle of size `n`. It assumes the size parameter `n` is an integer and returns an empty list if `n` is less than or equal to `0`.

* **13. Search and update**
  * [100-append_after.py](./100-append_after.py): This Python function inserts a line of text into a file after each line that contains a specified string.

* **14. Log parsing**
  * [101-stats.py](./101-stats.py): This Python script reads lines from standard input. After every 10 lines or when a keyboard interruption (`CTRL + C`) occurs, it computes the following metrics:
    * Total file size up to that point: `File size: <total size>`
    * Status code of each read line, printed in ascending order:  `<status code>: <number>`
  * Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`

Feel free to explore each task and its corresponding Python file for detailed implementation and usage instructions.