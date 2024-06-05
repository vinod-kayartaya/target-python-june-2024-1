#! .venv/bin/python
from myutils import line

class ExampleClass:
    class_data = []  # shared across all objects (only mutable types)

    def __init__(self) -> None:
        self.object_data = []  # data is restricted to a specific object (both mutable and immutable types)


def main():
    line()
    ec1 = ExampleClass()
    ec2 = ExampleClass()


    ec1.class_data.append(100)
    ec2.class_data.append(200)
    ExampleClass.class_data.append(300)

    ec1.object_data.append(10)
    ec2.object_data.append(20)

    print(f'{ec1.class_data = }')
    print(f'{ec2.class_data = }')
    print(f'{ec1.object_data = }')
    print(f'{ec2.object_data = }')

    print(f'{id(ec1.class_data) = }')
    print(f'{id(ec2.class_data) = }')
    print(f'{id(ec1.object_data) = }')
    print(f'{id(ec2.object_data) = }')

    line()


if __name__ == '__main__':
    main()

