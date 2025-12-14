# Python Programming Basics

A comprehensive guide to fundamental Python programming concepts.

## Table of Contents
1. [Introduction](#introduction)
2. [Variables and Data Types](#variables-and-data-types)
3. [Operators](#operators)
4. [Control Flow](#control-flow)
5. [Functions](#functions)
6. [Data Structures](#data-structures)
7. [File I/O](#file-io)
8. [Object-Oriented Programming Basics](#object-oriented-programming-basics)
9. [Common Built-in Functions](#common-built-in-functions)
10. [Best Practices](#best-practices)

---

## Introduction

Python is a high-level, interpreted programming language known for its simplicity and readability. It's widely used for web development, data analysis, automation, artificial intelligence, and more.

### Why Python?
- **Easy to learn**: Clear, readable syntax
- **Versatile**: Used in many domains
- **Large community**: Extensive libraries and support
- **Cross-platform**: Runs on Windows, macOS, Linux

---

## Variables and Data Types

### Variables
Variables store data values. In Python, you don't need to declare the type explicitly.

```python
# Variable assignment
name = "Alice"
age = 30
height = 5.6
is_student = True
```

### Basic Data Types

#### 1. Integers (int)
Whole numbers without decimal points.
```python
count = 10
negative = -5
```

#### 2. Floats (float)
Numbers with decimal points.
```python
price = 19.99
temperature = -3.5
```

#### 3. Strings (str)
Text data enclosed in quotes.
```python
message = "Hello, World!"
single_quotes = 'Python'
multiline = """This is a
multiline string"""
```

#### 4. Booleans (bool)
True or False values.
```python
is_active = True
is_deleted = False
```

#### 5. NoneType
Represents the absence of a value.
```python
result = None
```

### Type Conversion
```python
# String to integer
age = int("25")

# Integer to string
age_str = str(25)

# String to float
price = float("19.99")

# Integer to float
decimal = float(10)
```

---

## Operators

### Arithmetic Operators
```python
a = 10
b = 3

addition = a + b        # 13
subtraction = a - b     # 7
multiplication = a * b  # 30
division = a / b        # 3.333...
floor_division = a // b # 3
modulus = a % b         # 1
exponentiation = a ** b # 1000
```

### Comparison Operators
```python
x = 5
y = 10

equal = x == y          # False
not_equal = x != y      # True
greater = x > y         # False
less = x < y            # True
greater_equal = x >= y  # False
less_equal = x <= y     # True
```

### Logical Operators
```python
a = True
b = False

and_result = a and b    # False
or_result = a or b      # True
not_result = not a      # False
```

### Assignment Operators
```python
x = 5
x += 3  # x = x + 3 → 8
x -= 2  # x = x - 2 → 6
x *= 4  # x = x * 4 → 24
x /= 3  # x = x / 3 → 8.0
```

---

## Control Flow

### If-Elif-Else Statements
```python
age = 18

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
else:
    print("Adult")
```

### For Loops
```python
# Iterate over a range
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterate with index
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

### While Loops
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### Loop Control
```python
# Break: exit loop early
for i in range(10):
    if i == 5:
        break
    print(i)

# Continue: skip to next iteration
for i in range(5):
    if i == 2:
        continue
    print(i)
```

---

## Functions

### Defining Functions
```python
def greet(name):
    """Greet a person by name."""
    return f"Hello, {name}!"

message = greet("Alice")
print(message)
```

### Parameters and Arguments
```python
# Positional arguments
def add(a, b):
    return a + b

result = add(5, 3)

# Default parameters
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Bob"))              # Hello, Bob!
print(greet("Bob", "Hi"))        # Hi, Bob!

# Keyword arguments
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}")

describe_pet(animal="dog", name="Buddy")

# Variable arguments
def sum_all(*numbers):
    return sum(numbers)

total = sum_all(1, 2, 3, 4, 5)  # 15

# Keyword variable arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="NYC")
```

### Lambda Functions
Anonymous, inline functions.
```python
# Regular function
def square(x):
    return x ** 2

# Lambda equivalent
square = lambda x: x ** 2

# Common use with map, filter
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
```

---

## Data Structures

### Lists
Ordered, mutable collections.
```python
# Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", True, 3.14]

# Accessing elements
first = fruits[0]        # "apple"
last = fruits[-1]        # "cherry"

# Slicing
subset = numbers[1:4]    # [2, 3, 4]

# Modifying
fruits[1] = "blueberry"
fruits.append("orange")
fruits.insert(1, "grape")
fruits.remove("apple")
popped = fruits.pop()

# List operations
length = len(fruits)
sorted_list = sorted(numbers)
reversed_list = list(reversed(numbers))
```

### Tuples
Ordered, immutable collections.
```python
# Creating tuples
coordinates = (10, 20)
single = (1,)  # Note the comma for single-element tuple

# Accessing
x = coordinates[0]
y = coordinates[1]

# Unpacking
x, y = coordinates

# Tuples are immutable
# coordinates[0] = 5  # This would raise an error
```

### Dictionaries
Key-value pairs, unordered (before Python 3.7) or insertion-ordered (Python 3.7+).
```python
# Creating dictionaries
person = {
    "name": "Alice",
    "age": 30,
    "city": "NYC"
}

# Accessing values
name = person["name"]
age = person.get("age")  # Safer, returns None if key not found

# Modifying
person["age"] = 31
person["email"] = "alice@example.com"

# Removing
del person["city"]
email = person.pop("email")

# Dictionary operations
keys = person.keys()
values = person.values()
items = person.items()

# Iterating
for key, value in person.items():
    print(f"{key}: {value}")
```

### Sets
Unordered collections of unique elements.
```python
# Creating sets
numbers = {1, 2, 3, 4, 5}
unique = set([1, 2, 2, 3, 3, 4])  # {1, 2, 3, 4}

# Adding/removing
numbers.add(6)
numbers.remove(3)
numbers.discard(10)  # Doesn't error if not found

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

union = a | b           # {1, 2, 3, 4, 5, 6}
intersection = a & b    # {3, 4}
difference = a - b      # {1, 2}
symmetric_diff = a ^ b  # {1, 2, 5, 6}
```

---

## File I/O

### Reading Files
```python
# Read entire file
with open("file.txt", "r") as file:
    content = file.read()
    print(content)

# Read line by line
with open("file.txt", "r") as file:
    for line in file:
        print(line.strip())

# Read all lines into a list
with open("file.txt", "r") as file:
    lines = file.readlines()
```

### Writing Files
```python
# Write to file (overwrites)
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.")

# Append to file
with open("output.txt", "a") as file:
    file.write("\nAppended text")

# Write multiple lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)
```

### Working with CSV
```python
import csv

# Reading CSV
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Writing CSV
data = [
    ["Name", "Age", "City"],
    ["Alice", "30", "NYC"],
    ["Bob", "25", "LA"]
]

with open("output.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
```

---

## Object-Oriented Programming Basics

### Classes and Objects
```python
class Dog:
    """A simple Dog class."""

    # Class attribute
    species = "Canis familiaris"

    # Constructor
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age

    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

# Creating objects
buddy = Dog("Buddy", 3)
max_dog = Dog("Max", 5)

# Accessing attributes and methods
print(buddy.name)           # Buddy
print(buddy.bark())         # Buddy says Woof!
print(max_dog.description()) # Max is 5 years old
```

### Inheritance
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Using inherited classes
cat = Cat("Whiskers")
dog = Dog("Buddy")

print(cat.speak())  # Whiskers says Meow!
print(dog.speak())  # Buddy says Woof!
```

---

## Common Built-in Functions

### String Functions
```python
text = "  Hello, World!  "

# String methods
lower = text.lower()
upper = text.upper()
stripped = text.strip()
replaced = text.replace("World", "Python")
split_text = text.split(",")
joined = "-".join(["a", "b", "c"])  # "a-b-c"

# String checks
starts = text.startswith("  Hello")
ends = text.endswith("!")
is_digit = "123".isdigit()
is_alpha = "abc".isalpha()
```

### Math Functions
```python
import math

# Basic math
absolute = abs(-10)
rounded = round(3.14159, 2)
power = pow(2, 3)

# Math module
sqrt = math.sqrt(16)
ceil = math.ceil(3.2)
floor = math.floor(3.8)
pi = math.pi
```

### Collection Functions
```python
numbers = [1, 2, 3, 4, 5]

# Aggregation
total = sum(numbers)
maximum = max(numbers)
minimum = min(numbers)
length = len(numbers)

# Type conversion
tuple_nums = tuple(numbers)
set_nums = set(numbers)
list_from_range = list(range(5))

# Any/All
all_positive = all(x > 0 for x in numbers)
any_even = any(x % 2 == 0 for x in numbers)
```

---

## Best Practices

### 1. Use Meaningful Variable Names
```python
# Bad
x = 10
y = 20

# Good
width = 10
height = 20
```

### 2. Follow PEP 8 Style Guide
- Use 4 spaces for indentation
- Use snake_case for variables and functions
- Use PascalCase for class names
- Limit lines to 79 characters

### 3. Use Comments and Docstrings
```python
def calculate_area(radius):
    """
    Calculate the area of a circle.

    Args:
        radius (float): The radius of the circle

    Returns:
        float: The area of the circle
    """
    return math.pi * radius ** 2
```

### 4. Handle Exceptions
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Cleanup code here")
```

### 5. Use List Comprehensions
```python
# Instead of
squares = []
for i in range(10):
    squares.append(i ** 2)

# Use
squares = [i ** 2 for i in range(10)]
```

### 6. Use Context Managers for Resources
```python
# Always use 'with' for files
with open("file.txt", "r") as file:
    content = file.read()
# File is automatically closed
```

### 7. Use Enumerate Instead of Manual Indexing
```python
# Instead of
for i in range(len(items)):
    print(i, items[i])

# Use
for i, item in enumerate(items):
    print(i, item)
```

---

## Next Steps

After mastering these basics:
1. Learn about modules and packages
2. Explore advanced data structures (collections module)
3. Study exception handling in depth
4. Learn about decorators and generators
5. Explore popular libraries (NumPy, Pandas, Requests)
6. Practice with real projects

## Resources
- [Official Python Documentation](https://docs.python.org/)
- [Python.org Beginner's Guide](https://www.python.org/about/gettingstarted/)
- [PEP 8 Style Guide](https://pep8.org/)
- Practice platforms: LeetCode, HackerRank, Codewars

---

Happy Coding!
