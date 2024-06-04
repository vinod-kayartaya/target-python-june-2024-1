#! .venv/bin/python


# positional arguments (with default values, in this case)
def greet(name='friend', city = 'your city'):
    if type(name) is not str or type(city) is not str:
        raise TypeError('name and city must be str')
    
    print(f'Hello, {name}! How\'s weather in {city.title()}?')


# arbitrary arguments (variable length arguments)
def product(*args):
    # print(f'{type(args) = }')
    # print(f'{args = }')
    p = 1
    for each_arg in args:
        if type(each_arg) not in (int, float):
            continue
        p *= each_arg
    
    return p


def main():
    greet('Vinod', 'Bangalore')
    greet('Ramesh')
    greet(city=1234)
    greet()

    p = product(12, 3, 4, 'asd', False, 49, 10, 100)
    print(f'{p = }')


if __name__ == '__main__':
    main()

