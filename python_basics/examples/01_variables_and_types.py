"""
Python Basics: Variables and Data Types
This script demonstrates fundamental data types and variable usage in Python.
"""

print("=" * 50)
print("VARIABLES AND DATA TYPES")
print("=" * 50)

# 1. INTEGERS
print("\n1. INTEGERS (int)")
print("-" * 30)
age = 25
year = 2025
negative_number = -42

print(f"age = {age}, type: {type(age)}")
print(f"year = {year}, type: {type(year)}")
print(f"negative_number = {negative_number}, type: {type(negative_number)}")

# 2. FLOATING POINT NUMBERS
print("\n2. FLOATING POINT NUMBERS (float)")
print("-" * 30)
price = 19.99
temperature = -3.5
scientific = 1.5e3  # 1500.0

print(f"price = {price}, type: {type(price)}")
print(f"temperature = {temperature}, type: {type(temperature)}")
print(f"scientific notation (1.5e3) = {scientific}, type: {type(scientific)}")

# 3. STRINGS
print("\n3. STRINGS (str)")
print("-" * 30)
name = "Alice"
message = 'Hello, World!'
multiline = """This is a
multiline string"""

print(f"name = '{name}', type: {type(name)}")
print(f"message = '{message}', type: {type(message)}")
print(f"multiline = '''{multiline}''', type: {type(multiline)}")

# String operations
print("\nString Operations:")
print(f"Length of name: {len(name)}")
print(f"Uppercase: {name.upper()}")
print(f"Lowercase: {name.lower()}")
print(f"First character: {name[0]}")
print(f"Last character: {name[-1]}")
print(f"Slicing (first 3 chars): {name[:3]}")

# 4. BOOLEANS
print("\n4. BOOLEANS (bool)")
print("-" * 30)
is_active = True
is_deleted = False
comparison_result = 10 > 5

print(f"is_active = {is_active}, type: {type(is_active)}")
print(f"is_deleted = {is_deleted}, type: {type(is_deleted)}")
print(f"10 > 5 = {comparison_result}, type: {type(comparison_result)}")

# 5. NONE TYPE
print("\n5. NONE TYPE")
print("-" * 30)
result = None
print(f"result = {result}, type: {type(result)}")
print("None represents the absence of a value")

# 6. TYPE CONVERSION
print("\n6. TYPE CONVERSION")
print("-" * 30)

# String to Integer
age_string = "30"
age_int = int(age_string)
print(f"String '{age_string}' to int: {age_int}, type: {type(age_int)}")

# Integer to String
number = 42
number_string = str(number)
print(f"Int {number} to string: '{number_string}', type: {type(number_string)}")

# String to Float
price_string = "19.99"
price_float = float(price_string)
print(f"String '{price_string}' to float: {price_float}, type: {type(price_float)}")

# Integer to Float
int_number = 10
float_number = float(int_number)
print(f"Int {int_number} to float: {float_number}, type: {type(float_number)}")

# Float to Integer (truncates decimal)
float_val = 3.99
int_val = int(float_val)
print(f"Float {float_val} to int: {int_val}, type: {type(int_val)}")

# Boolean conversions
print(f"\nBool to int: True = {int(True)}, False = {int(False)}")
print(f"Int to bool: 1 = {bool(1)}, 0 = {bool(0)}, 42 = {bool(42)}")
print(f"String to bool: 'hello' = {bool('hello')}, '' = {bool('')}")

# 7. VARIABLE NAMING CONVENTIONS
print("\n7. VARIABLE NAMING BEST PRACTICES")
print("-" * 30)

# Good variable names (descriptive, lowercase with underscores)
user_name = "Alice"
total_price = 99.99
is_logged_in = True
max_retry_count = 5

print("Good variable names:")
print(f"  user_name = {user_name}")
print(f"  total_price = {total_price}")
print(f"  is_logged_in = {is_logged_in}")
print(f"  max_retry_count = {max_retry_count}")

# Constants (uppercase)
PI = 3.14159
MAX_USERS = 100
API_KEY = "your-api-key-here"

print("\nConstants (uppercase):")
print(f"  PI = {PI}")
print(f"  MAX_USERS = {MAX_USERS}")

# 8. MULTIPLE ASSIGNMENT
print("\n8. MULTIPLE ASSIGNMENT")
print("-" * 30)

# Assign same value to multiple variables
x = y = z = 0
print(f"x = y = z = 0: x={x}, y={y}, z={z}")

# Assign different values
a, b, c = 1, 2, 3
print(f"a, b, c = 1, 2, 3: a={a}, b={b}, c={c}")

# Swapping values
m, n = 10, 20
print(f"Before swap: m={m}, n={n}")
m, n = n, m
print(f"After swap: m={m}, n={n}")

# 9. INPUT FROM USER
print("\n9. USER INPUT (commented out for demonstration)")
print("-" * 30)
print("# To get user input:")
print("# name = input('Enter your name: ')")
print("# age = int(input('Enter your age: '))")  # Convert to int
print("# price = float(input('Enter price: '))")  # Convert to float

# 10. CHECKING TYPES
print("\n10. CHECKING TYPES")
print("-" * 30)

value1 = 42
value2 = "hello"
value3 = 3.14

print(f"Type of {value1}: {type(value1)}")
print(f"Type of '{value2}': {type(value2)}")
print(f"Type of {value3}: {type(value3)}")

print(f"\nIs {value1} an int? {isinstance(value1, int)}")
print(f"Is '{value2}' a string? {isinstance(value2, str)}")
print(f"Is {value3} a float? {isinstance(value3, float)}")

print("\n" + "=" * 50)
print("END OF VARIABLES AND DATA TYPES DEMO")
print("=" * 50)
