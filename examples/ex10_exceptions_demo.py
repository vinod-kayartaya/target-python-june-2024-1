#! .venv/bin/python
import sys


def main():
    try:
        arg1 = sys.argv[1]  # potential IndexError
        arg2 = sys.argv[2]  # potential IndexError

        n1 = int(arg1)  # potential ValueError
        n2 = int(arg2)  # potential ValueError

        q = n1 // n2  # potential ZeroDivisionError
        r = n1 % n2  # potential ZeroDivisionError
        
        print(f'{n1 = }')
        print(f'{n2 = }')
        print(f'{q = }')
        print(f'{r = }')
    except IndexError as err:
        print('Minimum 2 arguments expected for this program from CLI')
        print(f'{err = }')
    except ZeroDivisionError as err:
        print('Cannot divide a number by zero')
        print(f'{err = }')
        return  # finally block is executed before returning away from this function
    except ValueError as err:
        print('You must supply only integers')
        print(f'{err = }')
        exit(1)  # finally block is excecuted before exiting the application
    except Exception as err:
        print('Something went wrong!')
        print(f'{err = }')
    finally:
        print('The finally block is always executed and used for cleanups')

    print('End of main()')


if __name__ == '__main__':
    main()

