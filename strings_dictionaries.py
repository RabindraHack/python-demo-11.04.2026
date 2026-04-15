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






