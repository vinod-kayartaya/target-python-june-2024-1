#! .venv/bin/python
from dotenv import load_dotenv  # pin install python-dotenv
import os
from myutils import line


def main():
    line()
    password = os.getenv('password')
    print(f'{password = }')
    load_dotenv()
    password = os.getenv('password')
    print(f'{password = }')
    line()


if __name__ == '__main__':
    main()

