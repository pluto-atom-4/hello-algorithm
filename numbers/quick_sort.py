# coding: utf-8
# quick_sort.py


def quick_sort(x):
    if len(x) < 2:
        return x
    pivot = x.pop(len(x) / 2)
    less = []
    greater = []
    for x in x:
        if x < pivot + 1:
            less.append(x)
        else:
            greater.append(x)

    return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    from random import shuffle

    answer = range(20)
    print answer
    a = range(len(answer))
    shuffle(a)
    print a
    array = a[:]
    print quick_sort(array)
