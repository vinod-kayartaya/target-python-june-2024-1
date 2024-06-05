#! .venv/bin/python
from myutils import line


class Person(object):
    def __init__(self, **kwargs) -> None:
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')

    def print(self):
        print(f'Name         : {self.name}')
        print(f'Email        : {self.email}')


class Employee(Person):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        # Person.__init__(self, **kwargs)
        self.id = kwargs.get('id')
        self.salary = kwargs.get('salary')

    def print(self):
        print(f'ID           : {self.id}')
        super().print()
        print(f'Salary       : {self.salary}')




def main():
    line()
    emp1 = Employee(id=1234, name='Kishore', salary=50000, email='kishore@xmpl.com')
    emp2 = Employee(id=8272, name='Kiran', salary=60000, email='kiran@xmpl.com')
    # print(dir(emp1))

    emp1.print()
    print()
    emp2.print()
    line()


if __name__ == '__main__':
    main()

