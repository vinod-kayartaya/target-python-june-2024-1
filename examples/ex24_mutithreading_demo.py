#! .venv/bin/python
"""
- Thread
- GIL
"""
from threading import active_count, current_thread, Thread
import time
from myutils import line


def print_nums():
    for i in range(10):
        print(f'{i = } | {active_count() = } | {current_thread().name = }')
        time.sleep(0.5)


def print_chars():
    for ch in "mynameisvinod":
        print(f'{ch = } | {active_count() = } | {current_thread().name = }')
        time.sleep(0.25)

def play_bacground_music():
    while True:
        print('playing music in a loop...')
        time.sleep(0.1)

def main():
    line()
    print(f'{active_count() = }')
    print(f'{current_thread().name = }')

    t1 = Thread(target=print_chars, name='ThreadOne')
    t2 = Thread(target=print_nums, name='ThreadTwo')
    Thread(target=play_bacground_music, daemon=True).start()

    t1.start()
    t2.start()

    # for s in '!@#$%^&*()_+=-~`':
    #     print(f'{s = } | {active_count() = } | {current_thread().name = }')
    #     time.sleep(0.25)

    t1.join()
    t2.join()
    line()


if __name__ == '__main__':
    main()

