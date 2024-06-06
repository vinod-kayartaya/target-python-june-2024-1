#! .venv/bin/python
import time
import threading


def worker(n):
    print(f'Thread {n} is starting...')
    time.sleep(n)
    print(f'Finished the Thread {n} task')


def main():
    threads = []
    for i in range(1, 5):
        t = threading.Thread(target=worker, args=(i, ))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # at this time all threads have finished their tasks
    print('All threads have finished their tasks')
    

if __name__ == '__main__':
    main()

