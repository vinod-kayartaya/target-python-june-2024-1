#! .venv/bin/python
from myutils import line


class Employee(object):
    def __init__(self, **kwargs) -> None:
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.salary = kwargs.get('salary')

    def __str__(self) -> str:
        return f'Employee with id={self.id}, name={self.name}, salary={self.salary}'
    
    def __iadd__(self, value):
        if type(value) is str:
            self.name += value
        elif type(value) in (int, float):
            self.salary += value
        else:
            raise TypeError('Invalid type of value for += with an Employee object')
        
        return self

def main():
    line() 
    e1 = Employee(id=1121, name='Ramesh Kumar', salary=50000)
    e2 = Employee(id=2821, name='Kishore', salary=55000)

    print(e1)
    print(e2)

    e2 += ' Kulkarni'  # expectation is e2.name becomes 'Kishore Kulkarni'
    e2 += 7500  # expectation is e2.salary becomes 62500
    print(e2)

    line() 


if __name__ == '__main__':
    main()


"""
+       __add__
-       __sub__
*       __mul__
/       __div__
%       __mod__

Following functions must return self
+=       __iadd__
-=       __isub__
*=       __imul__
/=       __idiv__
%=       __imod__

Following functions must return bool
>       __gt__
>=       __ge__
<      __lt__
<=      __le__
==      __eq__
!=      __ne__

"""