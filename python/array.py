"""
Implement a dynamic array, similar to List
Interfaces:
- __getitem__
- __len__
- append(): insert at end, similar to push()
- remove(item): remove first match
- pop(): remove last (FILO)
- insertAt(index, item): insert at index position
- count(element): count all matching
- reverse()
- clear()

--- extra
? find(): return index of first match
"""

import ctypes

class myList(object):
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.data = self.makeArray(self.capacity)

    def __len__(self):
        return self.size

    def __getitem__(self, key):
        if not 0 <= key < self.size:
            return IndexError('Index is out of bounds')
        return self.data[key]

    def makeArray(self, capacity):
        temp = (capacity * ctypes.py_object)()
        return temp

    def append(self, item):
        # full capacity?
        if self.size == self.capacity:
            self._resize(self.capacity * 2 )
        
        self.data[self.size] = item
        self.size += 1 

    def _resize(self, newCapacity):
        newArray = self.makeArray(newCapacity)

        for i in range(self.size):
            newArray[i] = self.data[i]

        self.capacity = newCapacity
        self.data = newArray

    def __repr__(self):
        if self.size:
            return ', '.join(self.data[:self.size])
        else:
            return ''

    def pop(self):
        if not self.__len__():
            return ValueError('Empty list')
        
        retval = self.data[self.size-1] 
        self.data[self.size-1] = None
        self.size -= 1

        return retval

    def insertAt(self, position, item):
        if 0 < position >= self.size:
            return ValueError(position + ' out of bounds')
        
        self.append(self.data[self.size - 1])
        for i in range(self.size-2, position,-1 ):
            self.data[i] = self.data[i-1]
        self.data[position] = item

    def count(self, item):
        counter = 0
        for i in range(self.size):
            if item == self.data[i]:
                counter+=1
        return counter

    def _find(self, item):
        for i in range(self.size):
            if item == self.data[i]:
                return i
        return -1

    def remove(self, item):
        position = self._find(item)
        if position >= 0 :
            for i in range(position, self.size-1, 1):
                self.data[i] = self.data[i+1]
        self.data[self.size-1]= None
        self.size -= 1
        
        if self.size <= self.capacity//2 :
            self._resize(self.capacity//2)

    def reverse(self):
        return self.data[::-1]

    def clear(self):
        self.capacity=1
        self.size = 0
        self.data=self.makeArray(self.capacity)


if __name__ == "__main__":
    arr = myList()

    # add item
    print('append:{} => {}'.format(arr.append('a'), arr))
    print('append:{} => {}'.format(arr.append('b'), arr))
    print('append:{} => {}'.format(arr.append('c'), arr))


    # remove/pop
    print('pop:{} => {}'.format(arr.pop(), arr))
    # print('pop:{} => {}'.format(arr.pop(), arr))

    # insertAt
    print('insertAt:{} => {}'.format(arr.insertAt(0, 'c'), arr))
    # count
    arr.append('a')
    print('count a: {} => {}'.format(arr.count('a'), arr))

    # remove
    arr.remove('a')
    arr.remove('a')
    print('remove:{} => {} capacity:{}'.format('', arr, arr.capacity))

    # reverse
    print('reverse:', arr.reverse())

    # clear
    arr.clear()
    print('clear: ', arr)

