# Squared simple

📝 **Description:** This function computes the square value of all integers of a matrix.

**Prototype:** `def square_matrix_simple(matrix=[])`\
* `matrix` is a 2-dimensional array

**Returns:**\
A new matrix:
- Same size as `matrix`
- Each value should be the square of the value of the input
- Initial matrix should not be modified

**Constraints:**
- You are not allowed to import any module
- You are allowed to use regular loops, map, etc.

---

# Search and replace

📝 **Description:** This function replaces all occurrences of an element by another in a new list.

**Prototype:** `def search_replace(my_list, search, replace)`\
* `my_list` is the initial list
* `search` is the element to replace in the list
* `replace` is the new element

**Returns:**\
A new list with replaced elements.

**Constraints:**
- You are not allowed to import any module

---

# Unique addition

📝 **Description:** This function adds all unique integers in a list (only once for each integer).

**Prototype:** `def uniq_add(my_list=[])`

**Returns:**\
The sum of all unique integers in the list.

**Constraints:**
- You are not allowed to import any module

---

# Present in both

📝 **Description:** This function returns a set of common elements in two sets.

**Prototype:** `def common_elements(set_1, set_2)`

**Returns:**\
A set containing the common elements found in both sets.

**Constraints:**
- You are not allowed to import any module

---

# Only differents

📝 **Description:** This function returns a set of all elements present in only one set.

**Prototype:** `def only_diff_elements(set_1, set_2)`

**Returns:**\
A set containing the elements that are present in only one of the two sets.

**Constraints:**
- You are not allowed to import any module

---

# Number of keys

📝 **Description:** This function returns the number of keys in a dictionary.

**Prototype:** `def number_keys(a_dictionary)`

**Returns:**\
The number of keys in the dictionary.

**Constraints:**
- You are not allowed to import any module

---

# Print sorted dictionary

📝 **Description:** This function prints a dictionary by ordered keys.

**Prototype:** `def print_sorted_dictionary(a_dictionary)`

**Notes:**
- You can assume that all keys are strings
- Keys should be sorted by alphabetic order
- Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary)
- Dictionary values can have any type

**Constraints:**
- You are not allowed to import any module

---

# Update dictionary

📝 **Description:** This function replaces or adds key/value in a dictionary.

**Prototype:** `def update_dictionary(a_dictionary, key, value)`

**Notes:**
- `key` argument will always be a string
- `value` argument can be of any type
- If a key exists in the dictionary, the value will be replaced
- If a key doesn’t exist in the dictionary, it will be created

**Constraints:**
- You are not allowed to import any module

---

# Simple delete by key

📝 **Description:** This function deletes a key in a dictionary.

**Prototype:** `def simple_delete(a_dictionary, key="")`

**Notes:**
- `key` argument will always be a string
- If a key doesn’t exist, the dictionary won’t change

**Constraints:**
- You are not allowed to

 import any module

---

# Multiply by 2

📝 **Description:** This function returns a new dictionary with all values multiplied by 2.

**Prototype:** `def multiply_by_2(a_dictionary)`

**Notes:**
- You can assume that all values are only integers

**Returns:**\
A new dictionary with all values multiplied by 2.

**Constraints:**
- You are not allowed to import any module

---

# Best score

📝 **Description:** This function returns a key with the biggest integer value.

**Prototype:** `def best_score(a_dictionary)`

**Notes:**
- You can assume that all values are only integers
- If no score is found, return `None`
- You can assume all students have a different score

**Returns:**\
The key with the biggest integer value, or `None` if no score is found.

**Constraints:**
- You are not allowed to import any module

---

# Multiply by using map

📝 **Description:** This function returns a list with all values multiplied by a number without using any loops.

**Prototype:** `def multiply_list_map(my_list=[], number=0)`

**Returns:**\
A new list:
- Same length as `my_list`
- Each value should be multiplied by `number`
- Initial list should not be modified

**Constraints:**
- You are not allowed to import any module
- You have to use map
- Your file should be max 3 lines

---

# Roman to Integer

📝 **Description:** Technical interview preparation: Convert a Roman numeral to an integer.

**Prototype:** `def roman_to_int(roman_string)`

**Notes:**
- You are not allowed to google anything
- Whiteboard first
- You can assume the number will be between 1 to 3999.
- `roman_to_int(roman_string)` must return an integer
- If the `roman_string` is not a string or `None`, return 0.