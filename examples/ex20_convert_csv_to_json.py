#! .venv/bin/python
import csv
import json
from myutils import line
import time

def main():
    line()
    filename = input('Enter CSV file to open: ')
    if filename[-4:] != '.csv':
        raise ValueError('Invalid filename. Must be a .csv file')
    
    data = []
    with open(filename, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    outfilename = filename[:-4]+f'{time.time()}.json'
    with open(outfilename, 'wt', encoding='utf-8') as file:
        json.dump(data, file)
        # json.dump(data, file, indent=4)
        print(f'data written to {outfilename}')

if __name__ == '__main__':
    main()

