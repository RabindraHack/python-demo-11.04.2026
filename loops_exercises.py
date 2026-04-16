"""
LOOPS - PRACTICAL EXERCISES
Problem-solving with loops
"""

print("=" * 70)
print("EXERCISE 1: Print numbers 1 to 10")
print("=" * 70)
for i in range(1, 11):
    print(i, end=" ")
print("\n")

print("=" * 70)
print("EXERCISE 2: Print squares of numbers 1 to 5")
print("=" * 70)
for i in range(1, 6):
    print(f"{i}² = {i**2}")
print()

print("=" * 70)
print("EXERCISE 3: Sum of numbers from 1 to 100")
print("=" * 70)
total = 0
for i in range(1, 101):
    total += i
print(f"Sum of 1 to 100: {total}\n")

print("=" * 70)
print("EXERCISE 4: Multiplication table of 5")
print("=" * 70)
num = 5
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
print()

print("=" * 70)
print("EXERCISE 5: Print odd numbers from 1 to 20")
print("=" * 70)
for i in range(1, 21):
    if i % 2 != 0:
        print(i, end=" ")
print("\n")

print("=" * 70)
print("EXERCISE 6: Count vowels in a string")
print("=" * 70)
text = "Python Programming"
vowels = "aeiouAEIOU"
vowel_count = 0
for char in text:
    if char in vowels:
        vowel_count += 1
print(f"Text: '{text}'")
print(f"Vowel count: {vowel_count}\n")

print("=" * 70)
print("EXERCISE 7: Find minimum and maximum in a list")
print("=" * 70)
numbers = [45, 23, 89, 12, 67, 34]
min_num = numbers[0]
max_num = numbers[0]
for num in numbers:
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num
print(f"Numbers: {numbers}")
print(f"Minimum: {min_num}")
print(f"Maximum: {max_num}\n")

print("=" * 70)
print("EXERCISE 8: Factorial of a number")
print("=" * 70)
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Factorial of {n}: {factorial}\n")

print("=" * 70)
print("EXERCISE 9: Print times table (1-3)")
print("=" * 70)
for i in range(1, 4):
    print(f"\nTimes table of {i}:")
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j}")

print("\n" + "=" * 70)
print("EXERCISE 10: Reverse a list without using reverse()")
print("=" * 70)
original_list = [1, 2, 3, 4, 5]
reversed_list = []
for i in range(len(original_list) - 1, -1, -1):
    reversed_list.append(original_list[i])
print(f"Original: {original_list}")
print(f"Reversed: {reversed_list}\n")

print("=" * 70)
print("EXERCISE 11: Check if a number is prime")
print("=" * 70)
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

test_numbers = [2, 7, 10, 13, 20, 23]
for num in test_numbers:
    print(f"{num} is {'prime' if is_prime(num) else 'not prime'}")
print()

print("=" * 70)
print("EXERCISE 12: Print Fibonacci sequence (first 10 numbers)")
print("=" * 70)
a, b = 0, 1
print(f"Fibonacci sequence (first 10):")
for i in range(10):
    print(a, end=" ")
    a, b = b, a + b
print("\n")

print("=" * 70)
print("EXERCISE 13: Count occurrences of each character")
print("=" * 70)
text = "hello world"
char_count = {}
for char in text:
    if char != " ":
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
print(f"Text: '{text}'")
print(f"Character count: {char_count}\n")

print("=" * 70)
print("EXERCISE 14: Find common elements in two lists")
print("=" * 70)
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common = []
for element in list1:
    if element in list2 and element not in common:
        common.append(element)
print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Common elements: {common}\n")

print("=" * 70)
print("EXERCISE 15: Remove duplicates from a list")
print("=" * 70)
numbers = [1, 2, 2, 3, 3, 4, 5, 5, 5]
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print(f"Original: {numbers}")
print(f"Without duplicates: {unique}\n")
