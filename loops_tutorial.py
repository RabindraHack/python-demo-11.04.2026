"""
COMPREHENSIVE LOOPS TUTORIAL
Demonstrates different types of loops in Python: for, while, nested loops, and loop control statements
"""

print("=" * 60)
print("1. BASIC FOR LOOPS")
print("=" * 60)

# For loop with range
print("\n--- For loop with range ---")
for i in range(5):
    print(f"Number: {i}")

# For loop with list
print("\n--- For loop with list ---")
fruits = ["apple", "banana", "cherry", "mango"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# For loop with enumeration (index and value)
print("\n--- For loop with enumerate ---")
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"Index {index}: {color}")

# For loop with string
print("\n--- For loop with string ---")
word = "PYTHON"
for letter in word:
    print(f"Letter: {letter}")

# For loop with range (start, stop, step)
print("\n--- For loop with range (start, stop, step) ---")
for num in range(0, 10, 2):
    print(f"Even number: {num}")

print("\n" + "=" * 60)
print("2. WHILE LOOPS")
print("=" * 60)

# Basic while loop
print("\n--- Basic while loop ---")
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1

# While loop with user input (password validation)
print("\n--- While loop - Password validation ---")
# while True:
#     password = input("Enter password (8 characters): ")
#     if len(password) == 8:
#         print("Password accepted!")
#         break
#     else:
#         print("Password must be 8 characters. Try again.")

# While loop with condition
print("\n--- While loop with condition ---")
num = 10
while num >= 1:
    print(f"Countdown: {num}")
    num -= 1

print("\n" + "=" * 60)
print("3. NESTED LOOPS")
print("=" * 60)

# Nested for loops - Multiplication table
print("\n--- Nested loops - Multiplication Table ---")
print("Times Table (2x2 grid):")
for i in range(1, 3):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}", end="  |  ")
    print()  # New line after inner loop

# Nested loops - Pattern
print("\n--- Nested loops - Pattern ---")
print("Star Pattern:")
for i in range(1, 4):
    for j in range(i):
        print("*", end=" ")
    print()

# Nested loops - Matrix
print("\n--- Nested loops - Matrix ---")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matrix elements:")
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

print("\n" + "=" * 60)
print("4. LOOP CONTROL STATEMENTS")
print("=" * 60)

# Break statement
print("\n--- Break statement ---")
for i in range(10):
    if i == 5:
        print(f"Breaking at {i}")
        break
    print(f"Iteration: {i}")

# Continue statement
print("\n--- Continue statement ---")
print("Printing odd numbers from 0-10:")
for i in range(11):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()

# Break in nested loop
print("\n--- Break in nested loop (breaks inner loop only) ---")
for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(f"i={i}, j={j}", end="  |  ")
    print()

print("\n" + "=" * 60)
print("5. PRACTICAL EXAMPLES")
print("=" * 60)

# Sum of numbers
print("\n--- Sum of numbers ---")
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(f"Sum of {numbers}: {total}")

# Checking scores (passing grades)
print("\n--- Passing grades (>= 46) ---")
scores = [95, 45, 87, 32, 91, 50, 20]
for score in scores:
    if score >= 46:
        print(f"Passing: {score}")
    else:
        print(f"Failing: {score}")

# Dictionary iteration
print("\n--- Iterating through dictionary ---")
student_info = {
    'name': 'Alice',
    'age': 22,
    'grade': 'A'
}
for key, value in student_info.items():
    print(f"{key}: {value}")

# List comprehension (alternative to for loop)
print("\n--- List comprehension (alternative to loops) ---")
# Instead of: for i in range(1, 6): result.append(i**2)
squares = [i**2 for i in range(1, 6)]
print(f"Squares: {squares}")

# Filtering with list comprehension
even_numbers = [num for num in range(1, 11) if num % 2 == 0]
print(f"Even numbers: {even_numbers}")

print("\n" + "=" * 60)
print("6. ADVANCED LOOP PATTERNS")
print("=" * 60)

# Loop with else
print("\n--- For loop with else (executes if loop completes without break) ---")
for i in range(3):
    print(f"Loop iteration: {i}")
else:
    print("Loop completed successfully!")

# For loop with break and else
print("\n--- For loop with break and else (else won't execute) ---")
for i in range(5):
    if i == 2:
        print(f"Breaking at {i}")
        break
    print(f"Iteration: {i}")
else:
    print("This won't print because of break")

# Multiple variables in zip
print("\n--- Loop with zip (multiple lists) ---")
names = ["Alice", "Bob", "Charlie"]
ages = [22, 25, 28]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Reverse iteration
print("\n--- Reverse iteration ---")
items = ["first", "second", "third"]
for item in reversed(items):
    print(item)

print("\n" + "=" * 60)
print("END OF LOOPS TUTORIAL")
print("=" * 60)
