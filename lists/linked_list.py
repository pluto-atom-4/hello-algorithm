# coding: utf-8
# linked_list.py
#

class LinkedList:

    class Cell:
        def __init__(self, data, link = None):
            self.data = data
            self.link = link

    def __init__(self, *args):
        self.top = LinkedList.Cell(None)
        for x in reversed(args):
            self.insert(0, x)

    def _nth(self, n):
        i = -1
        cp = self.top
        while cp is not None:
            if i == n:
                return cp
            i += 1
            cp = cp.link
        return None

    def insert(self, n, x):
        cp = self._nth(n - 1)
        if cp is not None:
            cp.link = LinkedList.Cell(x, cp.link)
            return x
        return None

    def at(self, n):
        cp = self._nth(n)
        if cp is not None:
            return cp.data
        return None

    def delete(self, n):
        cp = self._nth(n)
        if cp is not None and cp.link is not None:
            data = cp.link.data
            cp.link = cp.link.link
            return data
        return None

    def isEmpty(self):
        return self.top is None

    def __iter__(self):
        self.index = self.top.link
        return self

    def next(self):
        if self.index is None:
            raise StopIteration
        data = self.index.data
        self.index = self.index.link
        return data

    def each(self):
        cp = self.top.link
        while cp is not None:
            yield cp.data
            cp = cp.link

    def __len__(self):
        n = 0
        for _ in self.each():
            n += 1
        return n

    def __getitem__(self, n):
        cp = self._nth(n)
        if cp is not None:
            return cp.data
        raise IndexError

    def __setitem__(self, n, value):
        cp = self._nth(n)
        if cp is not None:
            cp.data = value
            return None
        raise IndexError

    def __delitem__(self, n):
        if self.delete(n) is None:
            raise IndexError

    def __add__(x, y):
        def copy(a):
            if not a:
                return None
            return LinkedList.Cell(a.data, copy(a.link))
        def append(a, b):
            if a is None:
                return copy(b)
            return LinkedList.Cell(a.data, append(a.link, b))

        if not isinstance(y, LinkedList):
            raise NotImplementedError
        z = LinkedList()
        z.top.link = append(x.top.link, y.top.link)
        return z

    def __str__(self):
        if self.top.link is None:
            return 'LList()'
        s = 'LList('
        for x in self.each():
            s += '%s, ' % x
        return s[:-2] + ')'

if __name__ == '__main__':
    a = LinkedList()
    print a
    print len(a)
    print a.isEmpty()
    for x in xrange(5):
        a.insert(x, x)
    print a
    print len(a)
    print a.isEmpty()
    for x in xrange(5):
        a.insert(x,x)
    print a
    print a.isEmpty()
    for x in xrange(5):
        print a.at(x)
        print a[x]
    for x in xrange(5):
        a[x] = a[x] * 10
    for x in a:
        print x
    # while not a.isEmpty():
    #     del a[0]
    # print a
    a = LinkedList(1,2,3,4,5)
    b = LinkedList(6,7,8,9,10)
    c = a + b
    print a
    print b
    print c
    c[0] = 10
    c[5] = 60
    print a
    print b
    print c

