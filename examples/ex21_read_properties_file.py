#! .venv/bin/python
import configparser
from myutils import line


def main():
    line()
    parser = configparser.ConfigParser()
    parser.read('database-info.properties')

    host = parser.get('database', 'host')
    port = parser.getint('database', 'port')
    port1 = parser.get('database', 'port')
    dbname = parser.get('database', 'dbname')
    username = parser.get('database', 'username')
    password = parser.get('database', 'password')
    driver = parser.get('database', 'driver')

    print(f'{host = }')
    print(f'{port = }')
    print(f'{port1 = }')
    print(f'{dbname = }')
    print(f'{username = }')
    print(f'{password = }')
    print(f'{driver = }')
    line()


if __name__ == '__main__':
    main()

