"""
Python Basics: Exercise Solutions

Solutions to the practice exercises in exercises.py
"""

print("=" * 60)
print("PYTHON BASICS - EXERCISE SOLUTIONS")
print("=" * 60)

# SOLUTION 1: Variables and Data Types
print("\nSOLUTION 1: Variables and Data Types")
print("-" * 60)

name = "John Doe"
age = 25
height = 1.75
is_student = True

print(f"Name: {name}")
print(f"Age: {age} years old")
print(f"Height: {height} meters")
print(f"Student: {is_student}")

# SOLUTION 2: String Manipulation
print("\nSOLUTION 2: String Manipulation")
print("-" * 60)

text = "  Python Programming  "
print(f"Original: '{text}'")

# 1. Remove spaces
cleaned = text.strip()
print(f"Stripped: '{cleaned}'")

# 2. Uppercase
upper = cleaned.upper()
print(f"Uppercase: '{upper}'")

# 3. Replace
replaced = cleaned.replace("Programming", "Coding")
print(f"Replaced: '{replaced}'")

# 4. Count 'P'
count_p = cleaned.upper().count('P')
print(f"Count of 'P': {count_p}")

# 5. Split into words
words = cleaned.split()
print(f"Words: {words}")

# SOLUTION 3: Arithmetic Operations
print("\nSOLUTION 3: Arithmetic Operations")
print("-" * 60)

a, b = 15, 4
print(f"a = {a}, b = {b}")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Power: {a} ** {b} = {a ** b}")

# SOLUTION 4: Conditional Statements
print("\nSOLUTION 4: Conditional Statements")
print("-" * 60)

score = 85

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Score: {score}, Grade: {grade}")

# SOLUTION 5: For Loops
print("\nSOLUTION 5: For Loops")
print("-" * 60)

# 1. Numbers 1 to 10
print("Numbers 1 to 10:")
for i in range(1, 11):
    print(i, end=" ")
print()

# 2. Even numbers 1 to 20
print("\nEven numbers 1 to 20:")
for i in range(2, 21, 2):
    print(i, end=" ")
print()

# 3. Sum 1 to 100
total = 0
for i in range(1, 101):
    total += i
print(f"\nSum of 1 to 100: {total}")

# 4. Multiplication table for 7
print("\nMultiplication table for 7:")
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")

# SOLUTION 6: While Loops
print("\nSOLUTION 6: While Loops")
print("-" * 60)

# 1. Count down from 10
print("Countdown from 10:")
count = 10
while count >= 1:
    print(count, end=" ")
    count -= 1
print()

# 2. First number divisible by 3 and 7
print("\nFirst number divisible by both 3 and 7:")
num = 1
while True:
    if num % 3 == 0 and num % 7 == 0:
        print(f"Found: {num}")
        break
    num += 1

# 3. Factorial of 6
print("\nFactorial of 6:")
n = 6
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1
print(f"{n}! = {factorial}")

# SOLUTION 7: Lists
print("\nSOLUTION 7: Lists")
print("-" * 60)

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(f"Original list: {numbers}")

# 1. Length
print(f"Length: {len(numbers)}")

# 2. Sum
print(f"Sum: {sum(numbers)}")

# 3. Max and Min
print(f"Maximum: {max(numbers)}")
print(f"Minimum: {min(numbers)}")

# 4. Count 5s
print(f"Count of 5: {numbers.count(5)}")

# 5. Remove all 1s
numbers_copy = numbers.copy()
while 1 in numbers_copy:
    numbers_copy.remove(1)
print(f"After removing 1s: {numbers_copy}")

# 6. Sort descending
numbers_copy.sort(reverse=True)
print(f"Sorted descending: {numbers_copy}")

# 7. Top 3
top_3 = numbers_copy[:3]
print(f"Top 3 numbers: {top_3}")

# SOLUTION 8: List Comprehensions
print("\nSOLUTION 8: List Comprehensions")
print("-" * 60)

# 1. Squares 1-10
squares = [x ** 2 for x in range(1, 11)]
print(f"Squares: {squares}")

# 2. Even numbers 1-20
evens = [x for x in range(1, 21) if x % 2 == 0]
print(f"Evens: {evens}")

# 3. First letters
words = ["apple", "banana", "cherry"]
first_letters = [word[0] for word in words]
print(f"First letters: {first_letters}")

# 4. Divisible by 3
div_by_3 = [x for x in range(1, 21) if x % 3 == 0]
print(f"Divisible by 3: {div_by_3}")

# 5. Word lengths
words2 = ["hello", "world", "python", "programming"]
lengths = [len(word) for word in words2]
print(f"Word lengths: {lengths}")

# SOLUTION 9: Dictionaries
print("\nSOLUTION 9: Dictionaries")
print("-" * 60)

book = {
    "title": "Python Basics",
    "author": "John Doe",
    "year": 2024,
    "pages": 350
}

# 1. Print title and author
print(f"Title: {book['title']}")
print(f"Author: {book['author']}")

# 2. Add ISBN
book["isbn"] = "978-1234567890"
print(f"After adding ISBN: {book}")

# 3. Update year
book["year"] = 2025
print(f"After updating year: {book}")

# 4. All keys
print(f"Keys: {list(book.keys())}")

# 5. All values
print(f"Values: {list(book.values())}")

# 6. Check for publisher
print(f"'publisher' in book: {'publisher' in book}")

# SOLUTION 10: Sets
print("\nSOLUTION 10: Sets")
print("-" * 60)

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# 1. Union
print(f"Union: {set_a | set_b}")

# 2. Intersection
print(f"Intersection: {set_a & set_b}")

# 3. A - B
print(f"A - B: {set_a - set_b}")

# 4. B - A
print(f"B - A: {set_b - set_a}")

# 5. Symmetric difference
print(f"Symmetric difference: {set_a ^ set_b}")

# SOLUTION 11: Functions
print("\nSOLUTION 11: Functions")
print("-" * 60)

def is_even(number):
    """Check if number is even."""
    return number % 2 == 0

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def find_max(a, b, c):
    """Find maximum of three numbers."""
    return max(a, b, c)

def count_vowels(text):
    """Count vowels in text."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def reverse_string(text):
    """Reverse a string."""
    return text[::-1]

# Test functions
print(f"is_even(4): {is_even(4)}")
print(f"is_even(7): {is_even(7)}")
print(f"celsius_to_fahrenheit(25): {celsius_to_fahrenheit(25)}")
print(f"find_max(10, 25, 15): {find_max(10, 25, 15)}")
print(f"count_vowels('hello world'): {count_vowels('hello world')}")
print(f"reverse_string('python'): {reverse_string('python')}")

# SOLUTION 12: Calculator Function
print("\nSOLUTION 12: Calculator Function")
print("-" * 60)

def calculator(num1, num2, operation):
    """Perform arithmetic operations."""
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Unknown operation"

print(f"calculator(10, 5, 'add'): {calculator(10, 5, 'add')}")
print(f"calculator(10, 5, 'subtract'): {calculator(10, 5, 'subtract')}")
print(f"calculator(10, 5, 'multiply'): {calculator(10, 5, 'multiply')}")
print(f"calculator(10, 5, 'divide'): {calculator(10, 5, 'divide')}")
print(f"calculator(10, 0, 'divide'): {calculator(10, 0, 'divide')}")

# SOLUTION 13: Word Frequency Counter
print("\nSOLUTION 13: Word Frequency Counter")
print("-" * 60)

def word_frequency(text):
    """Count word frequencies."""
    words = text.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

text = "hello world hello python world hello"
result = word_frequency(text)
print(f"Text: '{text}'")
print(f"Frequency: {result}")

# SOLUTION 14: Prime Number Checker
print("\nSOLUTION 14: Prime Number Checker")
print("-" * 60)

def is_prime(n):
    """Check if n is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [num for num in range(1, 51) if is_prime(num)]
print(f"Prime numbers from 1 to 50: {primes}")

# SOLUTION 15: FizzBuzz
print("\nSOLUTION 15: FizzBuzz")
print("-" * 60)

def fizzbuzz(n):
    """Print FizzBuzz sequence."""
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
    print()

print("FizzBuzz(20):")
fizzbuzz(20)

# SOLUTION 16: List Filtering
print("\nSOLUTION 16: List Filtering")
print("-" * 60)

numbers_list = [12, -7, 3, -18, 25, -4, 9, -15, 30]
print(f"Original: {numbers_list}")

positive = [x for x in numbers_list if x > 0]
print(f"Positive: {positive}")

negative = [x for x in numbers_list if x < 0]
print(f"Negative: {negative}")

greater_10 = [x for x in numbers_list if x > 10]
print(f"Greater than 10: {greater_10}")

even = [x for x in numbers_list if x % 2 == 0]
print(f"Even: {even}")

# SOLUTION 17: Student Grade Manager
print("\nSOLUTION 17: Student Grade Manager")
print("-" * 60)

students = {
    "Alice": [85, 92, 88],
    "Bob": [79, 85, 91],
    "Charlie": [92, 88, 95]
}

# Calculate averages
averages = {}
for name, grades in students.items():
    avg = sum(grades) / len(grades)
    averages[name] = avg
    print(f"{name}'s average: {avg:.2f}")

# Highest average
highest_avg = max(averages.values())
top_student = [name for name, avg in averages.items() if avg == highest_avg][0]
print(f"\nHighest average: {highest_avg:.2f}")
print(f"Top student: {top_student}")

# Class average
all_grades = []
for grades in students.values():
    all_grades.extend(grades)
class_avg = sum(all_grades) / len(all_grades)
print(f"Class average: {class_avg:.2f}")

# SOLUTION 18: Palindrome Checker
print("\nSOLUTION 18: Palindrome Checker")
print("-" * 60)

def is_palindrome(text):
    """Check if text is a palindrome."""
    # Remove spaces and convert to lowercase
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

test_texts = [
    "A man a plan a canal Panama",
    "radar",
    "python",
    "racecar"
]

for text in test_texts:
    result = is_palindrome(text)
    print(f"'{text}' is palindrome: {result}")

# SOLUTION 19: Shopping Cart
print("\nSOLUTION 19: Shopping Cart")
print("-" * 60)

def add_to_cart(cart, item, price):
    """Add item to cart."""
    cart[item] = price
    return cart

def remove_from_cart(cart, item):
    """Remove item from cart."""
    if item in cart:
        del cart[item]
    return cart

def calculate_total(cart):
    """Calculate total price."""
    return sum(cart.values())

def apply_discount(total, discount_percent):
    """Apply discount to total."""
    discount = total * (discount_percent / 100)
    return total - discount

# Test shopping cart
cart = {}
cart = add_to_cart(cart, "Apple", 1.50)
cart = add_to_cart(cart, "Banana", 0.75)
cart = add_to_cart(cart, "Milk", 3.50)
print(f"Cart: {cart}")

total = calculate_total(cart)
print(f"Total: ${total:.2f}")

discounted = apply_discount(total, 10)
print(f"After 10% discount: ${discounted:.2f}")

cart = remove_from_cart(cart, "Banana")
print(f"After removing Banana: {cart}")
print(f"New total: ${calculate_total(cart):.2f}")

# SOLUTION 20: Contact Book
print("\nSOLUTION 20: Contact Book")
print("-" * 60)

contacts = {}

def add_contact(name, phone, email):
    """Add a new contact."""
    contacts[name] = {"phone": phone, "email": email}
    print(f"Added: {name}")

def remove_contact(name):
    """Remove a contact."""
    if name in contacts:
        del contacts[name]
        print(f"Removed: {name}")
    else:
        print(f"Contact {name} not found")

def find_contact(name):
    """Find and display a contact."""
    if name in contacts:
        print(f"{name}: {contacts[name]}")
        return contacts[name]
    else:
        print(f"Contact {name} not found")
        return None

def list_all_contacts():
    """List all contacts."""
    if not contacts:
        print("No contacts")
    else:
        for name, info in contacts.items():
            print(f"{name}: {info}")

def update_contact(name, phone, email):
    """Update contact information."""
    if name in contacts:
        contacts[name] = {"phone": phone, "email": email}
        print(f"Updated: {name}")
    else:
        print(f"Contact {name} not found")

# Test contact book
add_contact("Alice", "555-1234", "alice@example.com")
add_contact("Bob", "555-5678", "bob@example.com")
add_contact("Charlie", "555-9012", "charlie@example.com")

print("\nAll contacts:")
list_all_contacts()

print("\nFind Alice:")
find_contact("Alice")

print("\nUpdate Bob:")
update_contact("Bob", "555-9999", "bob.new@example.com")

print("\nRemove Charlie:")
remove_contact("Charlie")

print("\nFinal contact list:")
list_all_contacts()

print("\n" + "=" * 60)
print("END OF SOLUTIONS")
print("=" * 60)
