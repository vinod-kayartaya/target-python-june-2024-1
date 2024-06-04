#! .venv/bin/python

def main():
    nums = [200, 19, 28, 48, 29, 6, 20, 100, 99, 49]

    # even_nums = []
    # for n in nums:
    #     if n % 2 == 0:
    #         even_nums.append(n)

    even_nums = [n for n in nums if n % 2 == 0]
    odd_nums = [n for n in nums if n % 2]

    print(f'{even_nums = }')
    print(f'{odd_nums = }')

    names = ("vinod kumar", "SHYAM SUNDAR", "ramEsh KuMAR", "surya rao", "vijay")
    names_in_titlecase = [each_name.title() for each_name in names]
    print(f'{names_in_titlecase = }')

    first_names = [each_name.split(' ')[0].upper() for each_name in names]
    print(f'{first_names = }')

    to_code = lambda n: ''.join([c for c in n.replace(' ', '') if c.lower() not in 'aeiou']).upper()
    codes = [to_code(each_name) for each_name in names]
    print(f'{codes = }')

    name_lens = {name: len(name) for name in names_in_titlecase}
    print(f'{name_lens = }')

if __name__ == '__main__':
    main()

