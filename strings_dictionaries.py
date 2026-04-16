text = " python programming "
print(text.strip().title())

email = input('enter your choosen email here - : ')
if email.startswith('user') and '@' in email:
    print('correct email')
else:
    print('incorrect email')

student = {
    'name': 'Alice',
      'age': 22
    }
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

config = {'theme': 'dark'}
font_size = config.get('font_size', 1900)

print("Font Size:", font_size)

user = {
    'name': 'Alice',
    'address' : {
        'city': 'Bhubaneswar'
    }
}
city = user.get('address', {}).get('city', 'Not Found') 

print("City:", city)

# Function to find odd numbers in a list
def find_odd_numbers(numbers):
    """
    This function takes a list of numbers and returns a list of odd numbers.
    """
    return [num for num in numbers if num % 2 != 0]

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = find_odd_numbers(numbers)
print("Odd numbers:", odd_numbers)






