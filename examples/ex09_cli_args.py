#! .venv/bin/python
import sys


def is_float(s:str) -> bool:
    try:
        float(s)
        return True
    except:
        return False


def to_float(s: str) -> float:
    try:
        return float(s)
    except ValueError:
        return 0.0


def main():
    args = sys.argv[1:]
    print(f'{args = }')
    args = [float(arg) for arg in args if is_float(arg)]
    print(f'{args = }')
    total = sum(args)
    print(f'{total = }')

if __name__ == '__main__':
    main()

