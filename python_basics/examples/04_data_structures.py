"""
Python Basics: Data Structures
This script demonstrates lists, tuples, dictionaries, and sets in Python.
"""

print("=" * 50)
print("DATA STRUCTURES")
print("=" * 50)

# 1. LISTS - Ordered, Mutable Collections
print("\n1. LISTS")
print("-" * 30)

# Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
empty_list = []

print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Mixed types: {mixed}")
print(f"Empty list: {empty_list}")

# Accessing elements
print(f"\nFirst fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"Second fruit: {fruits[1]}")

# Slicing
print(f"\nFirst two numbers: {numbers[:2]}")
print(f"Last three numbers: {numbers[-3:]}")
print(f"Middle numbers: {numbers[1:4]}")
print(f"Every other number: {numbers[::2]}")
print(f"Reversed: {numbers[::-1]}")

# Modifying lists
print("\nModifying lists:")
fruits[1] = "blueberry"
print(f"After changing index 1: {fruits}")

fruits.append("orange")
print(f"After append: {fruits}")

fruits.insert(1, "grape")
print(f"After insert at index 1: {fruits}")

removed = fruits.remove("apple")  # Removes first occurrence
print(f"After remove 'apple': {fruits}")

popped = fruits.pop()  # Removes and returns last item
print(f"After pop (removed {popped}): {fruits}")

popped_index = fruits.pop(0)  # Remove at specific index
print(f"After pop(0) (removed {popped_index}): {fruits}")

# List operations
print("\nList operations:")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(f"Concatenation: {list1} + {list2} = {combined}")

repeated = list1 * 3
print(f"Repetition: {list1} * 3 = {repeated}")

print(f"Length of fruits: {len(fruits)}")
print(f"'cherry' in fruits: {'cherry' in fruits}")
print(f"Count of 'cherry': {fruits.count('cherry')}")

# Sorting
unsorted = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\nUnsorted: {unsorted}")
sorted_list = sorted(unsorted)  # Returns new sorted list
print(f"Sorted (new list): {sorted_list}")
print(f"Original unchanged: {unsorted}")

unsorted.sort()  # Sorts in place
print(f"After .sort(): {unsorted}")

unsorted.reverse()  # Reverses in place
print(f"After .reverse(): {unsorted}")

# List comprehensions
print("\nList comprehensions:")
squares = [x ** 2 for x in range(1, 6)]
print(f"Squares of 1-5: {squares}")

evens = [x for x in range(1, 11) if x % 2 == 0]
print(f"Even numbers 1-10: {evens}")

words = ["hello", "world", "python"]
uppercase = [word.upper() for word in words]
print(f"Uppercase: {uppercase}")

# 2. TUPLES - Ordered, Immutable Collections
print("\n2. TUPLES")
print("-" * 30)

# Creating tuples
coordinates = (10, 20)
rgb = (255, 128, 0)
single = (42,)  # Note: comma is required for single-element tuple
person = ("Alice", 30, "NYC")

print(f"Coordinates: {coordinates}")
print(f"RGB: {rgb}")
print(f"Single element: {single}")
print(f"Person: {person}")

# Accessing elements
print(f"\nX coordinate: {coordinates[0]}")
print(f"Y coordinate: {coordinates[1]}")
print(f"Name: {person[0]}, Age: {person[1]}, City: {person[2]}")

# Tuple unpacking
x, y = coordinates
print(f"Unpacked: x={x}, y={y}")

name, age, city = person
print(f"Unpacked person: {name}, {age}, {city}")

# Tuples are immutable
print("\nTuples are immutable:")
print("Cannot do: coordinates[0] = 15  # Would raise an error")

# Tuple operations
print("\nTuple operations:")
print(f"Length: {len(coordinates)}")
print(f"Concatenation: {coordinates + rgb}")
print(f"Repetition: {coordinates * 3}")
print(f"10 in coordinates: {10 in coordinates}")

# Why use tuples?
print("\nWhy use tuples?")
print("  - Immutable: Cannot be accidentally modified")
print("  - Faster: Slightly faster than lists")
print("  - Dictionary keys: Can be used as dict keys (lists cannot)")
print("  - Multiple return values: Functions often return tuples")

# 3. DICTIONARIES - Key-Value Pairs
print("\n3. DICTIONARIES")
print("-" * 30)

# Creating dictionaries
person = {
    "name": "Alice",
    "age": 30,
    "city": "NYC",
    "is_student": False
}

empty_dict = {}
dict_with_constructor = dict(name="Bob", age=25)

print(f"Person: {person}")
print(f"Empty dict: {empty_dict}")
print(f"Dict with constructor: {dict_with_constructor}")

# Accessing values
print(f"\nName: {person['name']}")
print(f"Age: {person.get('age')}")
print(f"Country: {person.get('country', 'Not specified')}")  # Default value

# Modifying dictionaries
print("\nModifying dictionaries:")
person["age"] = 31
print(f"Updated age: {person}")

person["email"] = "alice@example.com"
print(f"Added email: {person}")

del person["is_student"]
print(f"Deleted is_student: {person}")

email = person.pop("email")
print(f"Popped email ({email}): {person}")

# Dictionary operations
print("\nDictionary operations:")
print(f"Keys: {list(person.keys())}")
print(f"Values: {list(person.values())}")
print(f"Items: {list(person.items())}")
print(f"Length: {len(person)}")
print(f"'name' in person: {'name' in person}")

# Iterating dictionaries
print("\nIterating dictionary:")
for key in person:
    print(f"  {key}: {person[key]}")

print("\nIterating with items():")
for key, value in person.items():
    print(f"  {key} = {value}")

# Dictionary comprehension
print("\nDictionary comprehension:")
squares_dict = {x: x ** 2 for x in range(1, 6)}
print(f"Squares: {squares_dict}")

# Nested dictionaries
print("\nNested dictionaries:")
students = {
    "alice": {"age": 20, "grade": "A"},
    "bob": {"age": 22, "grade": "B"},
    "charlie": {"age": 21, "grade": "A"}
}
print(f"Students: {students}")
print(f"Alice's grade: {students['alice']['grade']}")

# Merging dictionaries (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = dict1 | dict2
print(f"\nMerged: {dict1} | {dict2} = {merged}")

# 4. SETS - Unordered, Unique Collections
print("\n4. SETS")
print("-" * 30)

# Creating sets
fruits_set = {"apple", "banana", "cherry"}
numbers_set = {1, 2, 3, 4, 5}
unique = set([1, 2, 2, 3, 3, 4])  # Duplicates removed
empty_set = set()  # Note: {} creates empty dict, not set

print(f"Fruits set: {fruits_set}")
print(f"Numbers set: {numbers_set}")
print(f"Unique (from list with duplicates): {unique}")

# Adding and removing
print("\nAdding and removing:")
fruits_set.add("orange")
print(f"After add: {fruits_set}")

fruits_set.remove("apple")  # Raises error if not found
print(f"After remove: {fruits_set}")

fruits_set.discard("mango")  # No error if not found
print(f"After discard (not in set): {fruits_set}")

# Set operations
print("\nSet operations:")
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(f"Set A: {a}")
print(f"Set B: {b}")

union = a | b
print(f"Union (A | B): {union}")

intersection = a & b
print(f"Intersection (A & B): {intersection}")

difference = a - b
print(f"Difference (A - B): {difference}")

symmetric_diff = a ^ b
print(f"Symmetric difference (A ^ B): {symmetric_diff}")

# Set methods
print("\nSet methods:")
print(f"a.union(b): {a.union(b)}")
print(f"a.intersection(b): {a.intersection(b)}")
print(f"a.difference(b): {a.difference(b)}")
print(f"a.symmetric_difference(b): {a.symmetric_difference(b)}")

# Set comparisons
print("\nSet comparisons:")
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print(f"set1.issubset(set2): {set1.issubset(set2)}")
print(f"set2.issuperset(set1): {set2.issuperset(set1)}")
print(f"set1.isdisjoint(set2): {set1.isdisjoint(set2)}")

# Set comprehension
print("\nSet comprehension:")
squares_set = {x ** 2 for x in range(1, 6)}
print(f"Squares: {squares_set}")

# 5. PRACTICAL EXAMPLES
print("\n5. PRACTICAL EXAMPLES")
print("-" * 30)

# Example 1: Count word frequency
text = "hello world hello python world hello"
words = text.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(f"Word frequency in '{text}':")
for word, count in word_count.items():
    print(f"  {word}: {count}")

# Example 2: Find unique elements
numbers_with_duplicates = [1, 2, 3, 2, 4, 1, 5, 3]
unique_numbers = list(set(numbers_with_duplicates))
print(f"\nOriginal: {numbers_with_duplicates}")
print(f"Unique: {unique_numbers}")

# Example 3: Group students by grade
students_list = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "Charlie", "grade": "A"},
    {"name": "David", "grade": "C"},
    {"name": "Eve", "grade": "B"}
]

by_grade = {}
for student in students_list:
    grade = student["grade"]
    if grade not in by_grade:
        by_grade[grade] = []
    by_grade[grade].append(student["name"])

print("\nStudents grouped by grade:")
for grade, names in sorted(by_grade.items()):
    print(f"  Grade {grade}: {', '.join(names)}")

# Example 4: Shopping cart
cart = {}

def add_item(item, quantity):
    if item in cart:
        cart[item] += quantity
    else:
        cart[item] = quantity

def remove_item(item, quantity):
    if item in cart:
        cart[item] -= quantity
        if cart[item] <= 0:
            del cart[item]

add_item("apple", 3)
add_item("banana", 2)
add_item("apple", 2)  # Add more apples
remove_item("banana", 1)

print("\nShopping cart:")
for item, qty in cart.items():
    print(f"  {item}: {qty}")

# Example 5: Find common elements in lists
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
common = list(set(list_a) & set(list_b))
print(f"\nCommon elements in {list_a} and {list_b}: {common}")

print("\n" + "=" * 50)
print("END OF DATA STRUCTURES DEMO")
print("=" * 50)
