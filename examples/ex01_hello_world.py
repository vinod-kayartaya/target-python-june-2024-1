"""
This is an example of using a python script. Usually the file (aka module) starts with a doc-string.
The docstring is used for documentation purposes.
"""

name = 'Shyam'
city = 'Shivamogga'

print('Hello,', name, '. How is weather in', city, '?')
print(f'Hello, {name}. How is weather in {city}?')

# following works in 3.12
print(f'{name = }')
print(f'{city = }')

