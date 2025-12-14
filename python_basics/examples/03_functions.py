"""
Python Basics: Functions
This script demonstrates function definition, parameters, return values, and advanced concepts.
"""

print("=" * 50)
print("FUNCTIONS")
print("=" * 50)

# 1. BASIC FUNCTION DEFINITION
print("\n1. BASIC FUNCTION DEFINITION")
print("-" * 30)

def greet():
    """Simple function with no parameters."""
    print("  Hello, World!")

print("Calling greet():")
greet()

# Function with return value
def get_greeting():
    """Function that returns a value."""
    return "Hello, Python!"

message = get_greeting()
print(f"Calling get_greeting(): {message}")

# 2. FUNCTIONS WITH PARAMETERS
print("\n2. FUNCTIONS WITH PARAMETERS")
print("-" * 30)

def greet_person(name):
    """Function with one parameter."""
    return f"Hello, {name}!"

print(greet_person("Alice"))
print(greet_person("Bob"))

def add(a, b):
    """Function with multiple parameters."""
    return a + b

result = add(5, 3)
print(f"add(5, 3) = {result}")

# 3. DEFAULT PARAMETERS
print("\n3. DEFAULT PARAMETERS")
print("-" * 30)

def greet_with_message(name, greeting="Hello"):
    """Function with default parameter."""
    return f"{greeting}, {name}!"

print(greet_with_message("Alice"))               # Uses default
print(greet_with_message("Bob", "Hi"))          # Overrides default
print(greet_with_message("Charlie", "Good morning"))

def power(base, exponent=2):
    """Calculate power with default exponent of 2."""
    return base ** exponent

print(f"\npower(5) = {power(5)}")         # 5^2 = 25
print(f"power(5, 3) = {power(5, 3)}")     # 5^3 = 125

# 4. KEYWORD ARGUMENTS
print("\n4. KEYWORD ARGUMENTS")
print("-" * 30)

def describe_pet(animal_type, pet_name):
    """Display pet information."""
    return f"I have a {animal_type} named {pet_name}"

# Positional arguments
print(describe_pet("dog", "Buddy"))

# Keyword arguments (order doesn't matter)
print(describe_pet(pet_name="Whiskers", animal_type="cat"))
print(describe_pet(animal_type="hamster", pet_name="Fluffy"))

# 5. VARIABLE-LENGTH ARGUMENTS (*args)
print("\n5. VARIABLE-LENGTH ARGUMENTS (*args)")
print("-" * 30)

def sum_all(*numbers):
    """Sum any number of arguments."""
    total = 0
    for num in numbers:
        total += num
    return total

print(f"sum_all(1, 2, 3) = {sum_all(1, 2, 3)}")
print(f"sum_all(1, 2, 3, 4, 5) = {sum_all(1, 2, 3, 4, 5)}")
print(f"sum_all(10, 20) = {sum_all(10, 20)}")

def print_args(*args):
    """Print all arguments."""
    print(f"  Received {len(args)} arguments:")
    for i, arg in enumerate(args, 1):
        print(f"    Arg {i}: {arg}")

print("\nCalling print_args('a', 'b', 'c', 'd'):")
print_args('a', 'b', 'c', 'd')

# 6. KEYWORD VARIABLE-LENGTH ARGUMENTS (**kwargs)
print("\n6. KEYWORD VARIABLE-LENGTH ARGUMENTS (**kwargs)")
print("-" * 30)

def print_info(**kwargs):
    """Print keyword arguments."""
    print("  Information received:")
    for key, value in kwargs.items():
        print(f"    {key}: {value}")

print("Calling print_info(name='Alice', age=30, city='NYC'):")
print_info(name="Alice", age=30, city="NYC")

def create_profile(name, **details):
    """Create a profile with name and additional details."""
    profile = f"Profile for {name}:"
    for key, value in details.items():
        profile += f"\n  {key}: {value}"
    return profile

print("\nCalling create_profile('Bob', age=25, job='Developer', city='SF'):")
print(create_profile("Bob", age=25, job="Developer", city="SF"))

# 7. COMBINING DIFFERENT PARAMETER TYPES
print("\n7. COMBINING PARAMETER TYPES")
print("-" * 30)

def full_function(pos1, pos2, default="default", *args, **kwargs):
    """Demonstrate all parameter types together."""
    print(f"  Positional 1: {pos1}")
    print(f"  Positional 2: {pos2}")
    print(f"  Default param: {default}")
    print(f"  *args: {args}")
    print(f"  **kwargs: {kwargs}")

print("Calling with various arguments:")
full_function("A", "B", "C", "D", "E", key1="value1", key2="value2")

# 8. RETURN MULTIPLE VALUES
print("\n8. RETURN MULTIPLE VALUES")
print("-" * 30)

def get_min_max(numbers):
    """Return both minimum and maximum values."""
    return min(numbers), max(numbers)

nums = [3, 1, 4, 1, 5, 9, 2, 6]
minimum, maximum = get_min_max(nums)
print(f"Numbers: {nums}")
print(f"Min: {minimum}, Max: {maximum}")

def divide_with_remainder(dividend, divisor):
    """Return quotient and remainder."""
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

q, r = divide_with_remainder(17, 5)
print(f"\n17 divided by 5: quotient={q}, remainder={r}")

# 9. LAMBDA FUNCTIONS
print("\n9. LAMBDA FUNCTIONS")
print("-" * 30)

# Regular function
def square(x):
    return x ** 2

# Lambda equivalent
square_lambda = lambda x: x ** 2

print(f"Regular function square(5) = {square(5)}")
print(f"Lambda function square_lambda(5) = {square_lambda(5)}")

# Lambda with multiple parameters
add_lambda = lambda a, b: a + b
print(f"add_lambda(3, 7) = {add_lambda(3, 7)}")

# Lambda with map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"\nNumbers: {numbers}")
print(f"Squared (using map): {squared}")

# Lambda with filter()
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers (using filter): {evens}")

# Lambda with sorted()
words = ["banana", "apple", "cherry", "date"]
sorted_by_length = sorted(words, key=lambda x: len(x))
print(f"\nWords: {words}")
print(f"Sorted by length: {sorted_by_length}")

# 10. DOCSTRINGS
print("\n10. DOCSTRINGS")
print("-" * 30)

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters:
        length (float): The length of the rectangle
        width (float): The width of the rectangle

    Returns:
        float: The area of the rectangle

    Example:
        >>> calculate_area(5, 3)
        15
    """
    return length * width

print(f"calculate_area(5, 3) = {calculate_area(5, 3)}")
print("\nFunction docstring:")
print(calculate_area.__doc__)

# 11. SCOPE (LOCAL VS GLOBAL)
print("\n11. SCOPE (LOCAL VS GLOBAL)")
print("-" * 30)

global_var = "I'm global"

def show_scope():
    local_var = "I'm local"
    print(f"  Inside function - Global: {global_var}")
    print(f"  Inside function - Local: {local_var}")

show_scope()
print(f"Outside function - Global: {global_var}")
# print(local_var)  # This would cause an error

# Modifying global variables
counter = 0

def increment():
    global counter  # Declare we're using global variable
    counter += 1
    print(f"  Counter inside function: {counter}")

print(f"\nCounter before: {counter}")
increment()
increment()
print(f"Counter after: {counter}")

# 12. RECURSION
print("\n12. RECURSION")
print("-" * 30)

def factorial(n):
    """Calculate factorial using recursion."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(f"factorial(5) = {factorial(5)}")  # 5! = 120
print(f"factorial(6) = {factorial(6)}")  # 6! = 720

def fibonacci(n):
    """Calculate nth Fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"\nFirst 10 Fibonacci numbers:")
for i in range(10):
    print(f"  fib({i}) = {fibonacci(i)}")

# 13. PRACTICAL EXAMPLES
print("\n13. PRACTICAL EXAMPLES")
print("-" * 30)

# Example 1: Temperature converter
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

print(f"25°C = {celsius_to_fahrenheit(25):.1f}°F")
print(f"77°F = {fahrenheit_to_celsius(77):.1f}°C")

# Example 2: Password validator
def is_valid_password(password):
    """
    Check if password meets criteria:
    - At least 8 characters
    - Contains uppercase and lowercase
    - Contains a digit
    """
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return has_upper and has_lower and has_digit

print(f"\nPassword validation:")
print(f"  'hello' is valid: {is_valid_password('hello')}")
print(f"  'Hello123' is valid: {is_valid_password('Hello123')}")

# Example 3: List statistics
def calculate_stats(numbers):
    """Calculate statistics for a list of numbers."""
    if not numbers:
        return None

    return {
        'count': len(numbers),
        'sum': sum(numbers),
        'mean': sum(numbers) / len(numbers),
        'min': min(numbers),
        'max': max(numbers)
    }

data = [12, 45, 23, 67, 34, 89, 56]
stats = calculate_stats(data)
print(f"\nStatistics for {data}:")
for key, value in stats.items():
    print(f"  {key}: {value}")

print("\n" + "=" * 50)
print("END OF FUNCTIONS DEMO")
print("=" * 50)
