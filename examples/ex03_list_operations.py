def main():
    """
    The list type has the following methods:
    ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

    Other builtin methods that can work on a list:
    len, sorted, reversed, map, filter
    """
    nums = [19, 28, 48, 29, 48, 48, 22, 46, 20]
    print(f'{len(nums) = }')
    print(f'{nums = }')

    # add at the end
    nums.append(100)
    # add at any given index
    nums.insert(0, 200)
    print(f'{nums = }')
    n = 48
    c = nums.count(n)
    print(f'{n} appears {c} times in the list')
    n = 77
    c = nums.count(n)
    print(f'{n} appears {c} times in the list')
    marks = [99, 49, 84]
    nums.append(marks)  # marks as an entire list will be append as a single element at the end
    print(f'{nums = }')
    nums.pop()
    nums.extend(marks)
    print(f'{nums = }')
    nums += marks  # same as .extend
    print(f'{nums = }')

    def is_odd(n):
        # print(f'{n = }')
        return n % 2  # 0 -> False, non-zero -> True
    
    odd_nums = list(filter(is_odd, nums))
    print(f'{odd_nums = }')

    even_nums = list(filter(lambda n:n%2==0, nums))
    print(f'{even_nums = }')


if __name__ == '__main__':
    main()
