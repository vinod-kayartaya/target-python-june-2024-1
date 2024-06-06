#! .venv/bin/python
import json
from myutils import line
import csv


def main():
    line()
    filename = input('Enter JSON file to open: ')
    if filename[-5:] != '.json':
        raise ValueError('Invalid filename. Must be a .json file')
    
    with open(filename, encoding='utf-8') as file:
        data = json.load(file)
        # customers = json.load(file, object_hook=lambda d:{'fullname': (d['first_name']+' '+d['last_name']).upper()})
        # customers = [c for c in customers if c['gender']=='Female']

        print(f'{type(data) = }')
        print(f'{len(data) = }')
        print(f'{type(data[0]) = }')
        print(f'{data[0] = }')
        
    # write the data into a CSV file
    outfilename = filename[:-5] + '.csv'
    with open(outfilename, 'wt', encoding='utf-8', newline='') as file:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
        print(f'created {outfilename} with all data.')

    line()


if __name__ == '__main__':
    main()

