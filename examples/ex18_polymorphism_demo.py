#! .venv/bin/python

from abc import ABC, abstractmethod
import math
from myutils import line


class Shape(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def print_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius = 1.0) -> None:
        super().__init__()
        self.radius = radius

    def print_area(self):
        area = math.pi * self.radius ** 2
        print(f'area of circle is {area}')


class Triangle(Shape):
    def __init__(self, base=1.0, height=1.0) -> None:
        super().__init__()
        self.base = base
        self.height = height

    def print_area(self):
        area = 0.5 * self.base * self.height
        print(f'area of triangle is {area}')


# polymorophic method
def process_shape(shape: Shape) -> None:
    if not isinstance(shape, Shape):
        raise TypeError('Invalid type for a Shape object')
    
    print('Got an object of a shape and here is the area of the same:')
    shape.print_area()


def main():
    line()
    c1 = Circle(12.34)
    t1 = Triangle(12.34, 56.78)

    process_shape(c1)
    process_shape(t1)
    # process_shape("vinod")
    line()


if __name__ == '__main__':
    main()
