"""
Python Basics: Practice Exercises

Complete these exercises to practice Python fundamentals.
Solutions are available in solutions.py - try solving them first!
"""

print("=" * 60)
print("PYTHON BASICS - PRACTICE EXERCISES")
print("=" * 60)

# EXERCISE 1: Variables and Data Types
print("\nEXERCISE 1: Variables and Data Types")
print("-" * 60)
print("""
Create variables for:
1. Your name (string)
2. Your age (integer)
3. Your height in meters (float)
4. Whether you are a student (boolean)

Then print all variables with descriptive messages.
""")

# Your code here:


# EXERCISE 2: String Manipulation
print("\nEXERCISE 2: String Manipulation")
print("-" * 60)
print("""
Given the string: "  Python Programming  "
1. Remove leading and trailing spaces
2. Convert to uppercase
3. Replace "Programming" with "Coding"
4. Count how many times 'P' appears (case-insensitive)
5. Split the string into a list of words
""")

text = "  Python Programming  "
# Your code here:


# EXERCISE 3: Arithmetic Operations
print("\nEXERCISE 3: Arithmetic Operations")
print("-" * 60)
print("""
Write a program that:
1. Takes two numbers: 15 and 4
2. Performs and prints: addition, subtraction, multiplication, division
3. Calculates floor division and modulus
4. Calculates 15 raised to the power of 4
""")

# Your code here:


# EXERCISE 4: Conditional Statements
print("\nEXERCISE 4: Conditional Statements")
print("-" * 60)
print("""
Write a program that checks a student's score and assigns a grade:
- 90-100: A
- 80-89: B
- 70-79: C
- 60-69: D
- Below 60: F

Test with score = 85
""")

# Your code here:


# EXERCISE 5: For Loops
print("\nEXERCISE 5: For Loops")
print("-" * 60)
print("""
1. Print numbers from 1 to 10
2. Print only even numbers from 1 to 20
3. Calculate the sum of numbers from 1 to 100
4. Print the multiplication table for 7 (1-10)
""")

# Your code here:


# EXERCISE 6: While Loops
print("\nEXERCISE 6: While Loops")
print("-" * 60)
print("""
1. Print numbers from 10 down to 1
2. Find the first number divisible by both 3 and 7 starting from 1
3. Calculate factorial of 6 using a while loop
""")

# Your code here:


# EXERCISE 7: Lists
print("\nEXERCISE 7: Lists")
print("-" * 60)
print("""
Given the list: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
1. Find and print the length
2. Find and print the sum
3. Find and print the maximum and minimum
4. Count how many times 5 appears
5. Remove all occurrences of 1
6. Sort the list in descending order
7. Get the 3 largest numbers
""")

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# Your code here:


# EXERCISE 8: List Comprehensions
print("\nEXERCISE 8: List Comprehensions")
print("-" * 60)
print("""
Create lists using list comprehensions:
1. Squares of numbers from 1 to 10
2. Even numbers from 1 to 20
3. First letter of each word in ["apple", "banana", "cherry"]
4. Numbers from 1 to 20 that are divisible by 3
5. Lengths of words in ["hello", "world", "python", "programming"]
""")

# Your code here:


# EXERCISE 9: Dictionaries
print("\nEXERCISE 9: Dictionaries")
print("-" * 60)
print("""
Create a dictionary representing a book with:
- title: "Python Basics"
- author: "John Doe"
- year: 2024
- pages: 350

Then:
1. Print the book's title and author
2. Add a new key "isbn" with value "978-1234567890"
3. Update the year to 2025
4. Print all keys
5. Print all values
6. Check if "publisher" is in the dictionary
""")

# Your code here:


# EXERCISE 10: Sets
print("\nEXERCISE 10: Sets")
print("-" * 60)
print("""
Given two sets:
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

Find and print:
1. Union of both sets
2. Intersection of both sets
3. Elements in set_a but not in set_b
4. Elements in set_b but not in set_a
5. Symmetric difference
""")

# Your code here:


# EXERCISE 11: Functions
print("\nEXERCISE 11: Functions")
print("-" * 60)
print("""
Write the following functions:

1. is_even(number): Returns True if number is even, False otherwise
2. celsius_to_fahrenheit(celsius): Converts Celsius to Fahrenheit
3. find_max(a, b, c): Returns the maximum of three numbers
4. count_vowels(text): Counts vowels in a string
5. reverse_string(text): Returns the reversed string
""")

# Your code here:


# EXERCISE 12: Advanced Function - Calculator
print("\nEXERCISE 12: Advanced Function - Calculator")
print("-" * 60)
print("""
Create a calculator function that:
- Takes three parameters: num1, num2, operation
- operation can be: 'add', 'subtract', 'multiply', 'divide'
- Returns the result of the operation
- Handles division by zero

Test with: calculator(10, 5, 'add') → 15
""")

# Your code here:


# EXERCISE 13: Word Frequency Counter
print("\nEXERCISE 13: Word Frequency Counter")
print("-" * 60)
print("""
Write a function that takes a string and returns a dictionary
with word frequencies.

Example:
text = "hello world hello python world hello"
Result: {'hello': 3, 'world': 2, 'python': 1}
""")

# Your code here:


# EXERCISE 14: Prime Number Checker
print("\nEXERCISE 14: Prime Number Checker")
print("-" * 60)
print("""
Write a function is_prime(n) that returns True if n is a prime number.
A prime number is only divisible by 1 and itself.

Then, print all prime numbers from 1 to 50.
""")

# Your code here:


# EXERCISE 15: FizzBuzz Function
print("\nEXERCISE 15: FizzBuzz Function")
print("-" * 60)
print("""
Write a function fizzbuzz(n) that prints numbers from 1 to n:
- Print "Fizz" if divisible by 3
- Print "Buzz" if divisible by 5
- Print "FizzBuzz" if divisible by both
- Otherwise print the number

Test with n=20
""")

# Your code here:


# EXERCISE 16: List Filtering
print("\nEXERCISE 16: List Filtering")
print("-" * 60)
print("""
Given a list of numbers: [12, -7, 3, -18, 25, -4, 9, -15, 30]

1. Filter positive numbers
2. Filter negative numbers
3. Filter numbers greater than 10
4. Filter even numbers

Use list comprehensions or filter() function.
""")

numbers_list = [12, -7, 3, -18, 25, -4, 9, -15, 30]
# Your code here:


# EXERCISE 17: Student Grade Manager
print("\nEXERCISE 17: Student Grade Manager")
print("-" * 60)
print("""
Create a program that manages student grades using a dictionary:

students = {
    "Alice": [85, 92, 88],
    "Bob": [79, 85, 91],
    "Charlie": [92, 88, 95]
}

Calculate and print:
1. Average grade for each student
2. Highest average
3. Student with highest average
4. Overall class average
""")

# Your code here:


# EXERCISE 18: Palindrome Checker
print("\nEXERCISE 18: Palindrome Checker")
print("-" * 60)
print("""
Write a function is_palindrome(text) that returns True if the text
is a palindrome (reads the same forwards and backwards).
Ignore case and spaces.

Test with: "A man a plan a canal Panama"
""")

# Your code here:


# EXERCISE 19: Shopping Cart
print("\nEXERCISE 19: Shopping Cart")
print("-" * 60)
print("""
Create a shopping cart system with functions:

1. add_to_cart(cart, item, price): Add item to cart
2. remove_from_cart(cart, item): Remove item from cart
3. calculate_total(cart): Calculate total price
4. apply_discount(total, discount_percent): Apply discount

Cart format: {"item": price, ...}

Test your functions with at least 3 items.
""")

# Your code here:


# EXERCISE 20: Advanced Challenge - Contact Book
print("\nEXERCISE 20: Advanced Challenge - Contact Book")
print("-" * 60)
print("""
Create a contact book system with these functions:

1. add_contact(name, phone, email): Add a new contact
2. remove_contact(name): Remove a contact
3. find_contact(name): Search for a contact
4. list_all_contacts(): Display all contacts
5. update_contact(name, phone, email): Update contact info

Store contacts in a dictionary or list of dictionaries.
Test all functions.
""")

# Your code here:


print("\n" + "=" * 60)
print("END OF EXERCISES")
print("See solutions.py for answers!")
print("=" * 60)
