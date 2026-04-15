   # cretate code like if password length == 8 then print correct password if not then ask for next password.
# while True:
#     password = input('Kindly Enter (8 Character ): - ')
#     if len(password) == 8:
#         print('correct password.')
#         break
#     else:
#         print('incorrect password (Try agin)')

# while True:
#     cmd = input("Command (quit to exit): ")
#     if cmd == "quit":
#         break
#         print(f"Running: {cmd}")
#     else:
#         print('Bla habani ja')

# for score in [95, 45, 87, 32, 91]:
#     if score < 46:
#         continue
#     print(f'passing- {score}')

# for i in range(3):
#     for j in range(3):
#         if j == 1:
#             break   # inner j-loop only
#         print(i, j)

# for i in [1, 2, 3]:
#     for j in ["A", "B", 'G', 'H']:
#         print(f"{i}{j}")

# for i in range(100):
#     print("Hello")

# i = 10
# for i in range(10000):
#     print("Hello Rabindra you became a milionair at 11/27/2027")

# count = 1

# while count <= 50000000000000:
#     print(count)
#     count += 1

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# def mul(a, b):
#     return a * b

# result = mul(5, 3)   # can use result later
# print(result)


student = {
    'name': 'Sahil',
    'age': 25,
    'city': 'Bhubaneswar'   
}
# student['age'] = 28
# student['village'] = 'Rajendranagar'
# print(student.get('age'))
# print(student.get('village'))

# for key, value in student.items():
#     print(key,value)

remove_value = student.pop('city')
print(remove_value)
print(student)
