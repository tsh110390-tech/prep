"""
Python Basics: Control Flow
This script demonstrates if statements, loops, and flow control in Python.
"""

print("=" * 50)
print("CONTROL FLOW")
print("=" * 50)

# 1. IF STATEMENTS
print("\n1. IF STATEMENTS")
print("-" * 30)

age = 18

if age < 13:
    status = "Child"
elif age < 20:
    status = "Teenager"
else:
    status = "Adult"

print(f"Age {age} is classified as: {status}")

# Multiple conditions
temperature = 25
is_raining = False

if temperature > 30 and not is_raining:
    print("It's hot and sunny - perfect for the beach!")
elif temperature > 20 and not is_raining:
    print("Nice weather for a walk!")
elif is_raining:
    print("Don't forget your umbrella!")
else:
    print("It's a bit cold outside.")

# 2. COMPARISON OPERATORS
print("\n2. COMPARISON OPERATORS")
print("-" * 30)

x = 10
y = 20

print(f"x = {x}, y = {y}")
print(f"x == y: {x == y}")  # Equal
print(f"x != y: {x != y}")  # Not equal
print(f"x > y: {x > y}")    # Greater than
print(f"x < y: {x < y}")    # Less than
print(f"x >= y: {x >= y}")  # Greater or equal
print(f"x <= y: {x <= y}")  # Less or equal

# 3. LOGICAL OPERATORS
print("\n3. LOGICAL OPERATORS")
print("-" * 30)

a = True
b = False

print(f"a = {a}, b = {b}")
print(f"a and b: {a and b}")   # Both must be True
print(f"a or b: {a or b}")     # At least one must be True
print(f"not a: {not a}")       # Negation

# Chaining comparisons
value = 15
print(f"\nIs {value} between 10 and 20?")
print(f"10 <= {value} <= 20: {10 <= value <= 20}")

# 4. FOR LOOPS
print("\n4. FOR LOOPS")
print("-" * 30)

# Loop through a range
print("Counting from 0 to 4:")
for i in range(5):
    print(f"  {i}", end=" ")
print()

# Loop with start, stop, step
print("\nEven numbers from 0 to 10:")
for i in range(0, 11, 2):
    print(f"  {i}", end=" ")
print()

# Loop through a list
fruits = ["apple", "banana", "cherry", "date"]
print(f"\nFruits list: {fruits}")
for fruit in fruits:
    print(f"  I like {fruit}!")

# Loop with index using enumerate
print("\nFruits with index:")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

# Loop with custom start index
print("\nFruits with index (starting at 1):")
for index, fruit in enumerate(fruits, start=1):
    print(f"  {index}. {fruit}")

# 5. WHILE LOOPS
print("\n5. WHILE LOOPS")
print("-" * 30)

# Basic while loop
count = 0
print("Counting with while loop:")
while count < 5:
    print(f"  Count: {count}")
    count += 1

# While loop with condition
print("\nDoubling until reaching 100:")
number = 1
while number < 100:
    print(f"  {number}", end=" ")
    number *= 2
print()

# 6. BREAK STATEMENT
print("\n6. BREAK STATEMENT")
print("-" * 30)

print("Finding first number divisible by 7:")
for i in range(1, 100):
    if i % 7 == 0:
        print(f"  Found: {i}")
        break  # Exit loop immediately

print("\nSearching for 'cherry' in fruits:")
for fruit in fruits:
    if fruit == "cherry":
        print(f"  Found {fruit}! Stopping search.")
        break
    print(f"  Checking {fruit}...")

# 7. CONTINUE STATEMENT
print("\n7. CONTINUE STATEMENT")
print("-" * 30)

print("Printing odd numbers from 1 to 10:")
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(f"  {i}", end=" ")
print()

print("\nSkipping vowels in 'PYTHON':")
word = "PYTHON"
for char in word:
    if char in "AEIOU":
        continue
    print(f"  {char}", end=" ")
print()

# 8. NESTED LOOPS
print("\n8. NESTED LOOPS")
print("-" * 30)

print("Multiplication table (1-5):")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i * j:4}", end=" ")
    print()  # New line after each row

print("\nPattern with nested loops:")
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

# 9. ELSE WITH LOOPS
print("\n9. ELSE WITH LOOPS")
print("-" * 30)

# For-else: else executes if loop completes without break
print("Searching for number > 100 in range(1, 10):")
for num in range(1, 10):
    if num > 100:
        print(f"  Found: {num}")
        break
else:
    print("  No number greater than 100 found")

# While-else example
print("\nCounting to 3 with while-else:")
counter = 0
while counter < 3:
    print(f"  Counter: {counter}")
    counter += 1
else:
    print("  Loop completed successfully!")

# 10. PASS STATEMENT
print("\n10. PASS STATEMENT")
print("-" * 30)

print("Using pass as a placeholder:")
for i in range(5):
    if i == 2:
        pass  # Do nothing, placeholder for future code
    else:
        print(f"  Number: {i}")

# Pass in functions and classes (placeholder)
def future_function():
    pass  # To be implemented later

class FutureClass:
    pass  # To be implemented later

print("  pass is useful as a placeholder for code to be written later")

# 11. CONDITIONAL EXPRESSIONS (TERNARY OPERATOR)
print("\n11. CONDITIONAL EXPRESSIONS")
print("-" * 30)

age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Age {age}: {status}")

# Another example
score = 85
grade = "Pass" if score >= 60 else "Fail"
print(f"Score {score}: {grade}")

# Nested ternary
score = 75
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D"
print(f"Score {score}: Grade {grade}")

# 12. PRACTICAL EXAMPLES
print("\n12. PRACTICAL EXAMPLES")
print("-" * 30)

# Example 1: Find all prime numbers up to 20
print("Prime numbers up to 20:")
primes = []
for num in range(2, 21):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
print(f"  {primes}")

# Example 2: FizzBuzz
print("\nFizzBuzz (1-20):")
for num in range(1, 21):
    if num % 15 == 0:
        print("  FizzBuzz", end=" ")
    elif num % 3 == 0:
        print("  Fizz", end=" ")
    elif num % 5 == 0:
        print("  Buzz", end=" ")
    else:
        print(f"  {num}", end=" ")
print()

# Example 3: Palindrome checker
word = "radar"
is_palindrome = word == word[::-1]
print(f"\nIs '{word}' a palindrome? {is_palindrome}")

word = "python"
is_palindrome = word == word[::-1]
print(f"Is '{word}' a palindrome? {is_palindrome}")

# Example 4: Sum of even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = 0
for num in numbers:
    if num % 2 == 0:
        even_sum += num
print(f"\nSum of even numbers in {numbers}: {even_sum}")

print("\n" + "=" * 50)
print("END OF CONTROL FLOW DEMO")
print("=" * 50)
