# coding: utf-8
# reverse_string.py: various function to reverse a strings
#

def reverse_a_string_slowly(a_string):
    new_string = ''
    index = len(a_string)
    while index:
        index -= 1
        new_string += a_string[index]
    return new_string


if __name__ == '__main__':
    original_string = 'hello python'
    print reverse_a_string_slowly(original_string)
    print original_string
