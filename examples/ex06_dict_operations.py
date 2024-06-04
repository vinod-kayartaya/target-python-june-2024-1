from pprint import pprint
# from myutils import dir2


def main():
    book1 = dict(title='Let us C', author='Y Kanitkar', price=299.9, page_count=255, publisher='BPB Publications')
    emp1 = {'fname': 'Rahul', 'lname': 'Khanna', 'salary': 78000, 'on_contract': False, 'department': 'PRODUCTION'}
    emp1['empno'] = 7872
    # emp1['commission'] = 5038

    pprint(book1)
    pprint(emp1)
    # print(dir2(dict))
    # methods in a dict: ['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

    # print(f'{emp1['fname']} earns a salary of ₹{emp1['salary']} and commission of ₹{emp1['commission']}')
    print(f'{emp1.get('fname')} earns a salary of ₹{emp1.get('salary')} and commission of ₹{emp1.get('commission', 0)}')

    emp2 = {key: value.upper() if type(value) is str else value
            for key, value in emp1.items()}
    
    print(f'{emp2 = }')
    print()
    print()

if __name__ == '__main__':
    main()

