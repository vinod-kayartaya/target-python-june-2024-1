import myutils  # myutils.__name__ will be 'myutils', which is the name of the file

# print(f'inside ex02_user_input.py, value of __name__ is {__name__}')
# inside this file (ex02_user_input.py), the value of __name__ is '__main__', since this is
# the file we are executing (or running)

# m = int(input('Enter month: (1-12) '))
# y = int(input('Enter year: (>=1) '))

m = 2
y = 2024

days = myutils.max_days(m, y)
print(f'Maximum days in month {m} of year {y} is {days}.')

