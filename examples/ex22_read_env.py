#! .venv/bin/python
import os
from myutils import line


def main():
    line()
    path = os.getenv('PATH')
    pythonpath = os.getenv('PYTHONPATH')
    maven_home = os.getenv('MAVEN_HOME')
    apache_home = os.getenv('APACHE_HOME')
    author_name = os.getenv('AUTHOR_NAME')
    my_name = os.getenv('MY_NAME')  # export MY_NAME="Vinod Kumar"

    print(f'{path = }')
    print(f'{pythonpath = }')
    print(f'{maven_home = }')
    print(f'{apache_home = }')
    print(f'{author_name = }')
    print(f'{my_name = }')

    os.environ['AUTHOR_NAME'] = 'Vinod'
    author_name = os.getenv('AUTHOR_NAME')
    print(f'{author_name = }')
    line()


if __name__ == '__main__':
    main()

