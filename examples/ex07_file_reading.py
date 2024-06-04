#! .venv/bin/python

FILENAME = 'myutils.py'


def file_read_method1():
    global FILENAME
    f = open(FILENAME, 'rt')
    content = f.read()
    f.close()

    print(content)


def file_read_method2():
    global FILENAME
    with open(FILENAME, 'rt') as f:  # context manager block; takes care of closing the resource
        # f.close() is called automatically when the current block exits
        content = f.read()
    print(content)


def file_read_method3():
    global FILENAME
    with open(FILENAME, 'rt') as f:
        for each_line in f:  # 'f' is a stream of lines from the file
            print(each_line, end='')


def main():
    file_read_method3()


if __name__ == '__main__':
    main()

