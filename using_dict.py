ab = {
    'Swaroop': 'swaroop@mail.com',
    'Who': 'who@mail.com',
    'Doctor': 'dr@mail.com'
     }

print('The Swaroop s address ', ab['Swaroop'])
# Delete key and value
del ab['Who']

print(f'The number of ab is {len(ab)}')

for name, address in ab.items():
    print(f'{name} have address {address}')
# Add new key and value
ab['Yazzz'] = 'yazzz@fish.com'
print(f"Yazzz have address {ab['Yazzz']}")
