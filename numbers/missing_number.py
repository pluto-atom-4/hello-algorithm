# coding: utf-8
# missing_number.py: finds the missing number for array

def find_missing_number(array):
    return sum(xrange(array[0], array[-1] + 1)) - sum(array)


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 7, 8, 9, 10]
    print find_missing_number(numbers)
