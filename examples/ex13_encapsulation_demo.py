#! .venv/bin/python


class Person:
    def __init__(self, **kwargs) -> None:
        self.name = kwargs.get('name')
        self.age = kwargs.get('age', 20)

    def __str__(self) -> str:
        return f'Person with name="{self.__name}" and age={self.__age}'
    
    # for each property (e.g, `name` or `age`) we must create two methods (one for setter and another for getter)
    # here is the getter
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if type(value) is not str:
            raise TypeError('name must be a str')
        if len(value) < 2 or len(value) > 20:
            raise ValueError('name must be between 2 to 20 letters')
        self.__name = value

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if type(value) not in (int, float):
            raise TypeError('age must be a number')
        if value < 1 or value > 130:
            raise ValueError('age must be between 1 and 130')
        self.__age = value


def main():
    p1 = Person(name='Vinod', age=500)
    print(f'p1.name is {p1.name} and p1.age is {p1.age}')
    p2 = Person()
    p2.name = 'Arun kumar'  # invokes the setter method `name`. In Java, p2.setName("Arun Kumar")
    # `p2` is the invoking object (becomes `self`) and `Arun` is the value
    p2.age = 29  # invokes the setter method `age`

    print(p1)
    print(p2)


if __name__ == '__main__':
    main()

