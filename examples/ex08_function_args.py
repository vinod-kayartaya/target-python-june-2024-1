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


def print_emp_details(**emp):  # the name `kwargs` is generally preferred for **variables
    # print(f'{type(emp) = }')
    # print(f'{emp = }')
    if 'fname' not in emp:  # by default the dict is considered as a collection of keys
        raise KeyError('the field `fname` is required but missing')
    
    print(f'ID         : {emp.get('id')}')
    print(f'Name       : {emp.get('fname')} {emp.get('lname', '')}')
    print(f'Saalary    : ₹ {emp.get('salary', 50000)}')
    print(f'Department : {emp.get('dept', 'SALES')}')
    print()


def main():
    # greet('Vinod', 'Bangalore')
    # greet('Ramesh')
    # greet(city='Mysore')
    # greet()

    # p = product(12, 3, 4, 'asd', False, 49, 10, 100)
    # print(f'{p = }')

    print_emp_details(id=1123, fname='Sujay', lname='Anand', salary=56780, dept='ADMIN')
    print_emp_details(id=1123, fname='Sujay', salary=56780)
    print_emp_details(id=1123, fname='Sujay', email='sujay@xmpl.com')
    print_emp_details(id=1123, email='sujay@xmpl.com')


if __name__ == '__main__':
    main()

