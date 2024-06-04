def main():
    nums = [200, 19, 28, 48, 29, 6, 20, 100, 99, 49]
    print(f'{len(nums) = }')
    print(f'{nums = }')
    index = 0
    print(f'nums[{index}] = {nums[index]}')
    index = 9
    print(f'nums[{index}] = {nums[index]}')
    index = -1
    print(f'nums[{index}] = {nums[index]}')
    index = -10
    print(f'nums[{index}] = {nums[index]}')

    print(f'{nums[3:7] = }')  # 4 (7-3) elements from index 3
    print(f'{nums[3:] = }')  # all elements from index 3
    print(f'{nums[:7] = }')  # all elements from index 0 till index 6

    print(f'{nums[2:9:2] = }')  # step value
    print(f'{nums[8:2:-1] = }')
    print(f'{nums[8::-1] = }')  # start from index 8 backwords till the start
    print(f'{nums[:2:-1] = }')  # start from end backwords till the index 2 (excluding)
    print(f'{nums[::-1] = }')  # all elements in reverse order

    my_name = 'vinod kumar'
    print(f'{my_name[::-1] = }')

if __name__ == '__main__':
    main()

