from abc import ABCMeta, abstractmethod

class Stack(metaclass=ABCMeta):
    """An interface for the stack data structure.

    A stack is a linear data structure that enforces last-in first-out (LIFO)
    ordering. That is, a stack is a collection of items that provides access to
    only the item added most recently. For example, suppose that Joe adds 17 to
    a stack, followed by 11 and then 19. He may remove 19, because it is the
    item he added most recently, but he may not remove 17 or 11. If Joe removes
    19, he may remove 11, because it is now the item he added most recently.
    Similarly, Joe may remove 17 only after he removes 11.
    
    Conceptually, a stack is vertical --- it has a top and a bottom. Client
    interaction is limited to the top of a stack. That is, the only location at
    which a client of a stack may add or remove an item is the top. A helpful
    analogy is to think of a stack of heavy items. For example, if you have a
    stack of 50 kg Olympic weights, the only location at which you can add or
    remove a weight is the top of the stack.
    """

    @abstractmethod
    def push(self, item):
        """Add an item to the top of the stack."""

    @abstractmethod
    def pop(self):
        """Removes and returns an item from the top of the stack."""

    @abstractmethod
    def top(self):
        """Returns the item at the top of the stack."""

    @abstractmethod
    def size(self):
        """Returns the number of items in the stack."""


class DynamicArrayStack(Stack):
    """A class that implements the Stack interface using a Python list."""

    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def top(self):
        return self._items[-1]

    def size(self):
        return len(self._items)


from collections import deque

class LinkedListStack(Stack):
    """A class that implements the Stack interface using a Python deque."""

    def __init__(self):
        self._items = deque()

    def push(self, item):
        self._items.appendleft(item)

    def pop(self):
        return self._items.popleft()

    def top(self):
        return self._items[0]

    def size(self):
        return len(self._items)


def main():
    stack = DynamicArrayStack()

    print('DynamicArrayStack push:', end='')
    for i in range(10):
        print(' {}'.format(i), end='')
        stack.push(i)
    print()

    top = stack.top()
    print('DynamicArrayStack top: {}'.format(top))

    size = stack.size()
    print('DynamicArrayStack size: {}'.format(size))
    for i in range(size):
        item = stack.pop()
        print('DynamicArrayStack pop: {}'.format(item))
    print()

    stack = LinkedListStack()

    print('LinkedListStack push:', end='')
    for i in range(10):
        print(' {}'.format(i), end='')
        stack.push(i)
    print()

    top = stack.top()
    print('LinkedListStack top: {}'.format(top))

    size = stack.size()
    print('LinkedListStack size: {}'.format(size))
    for i in range(size):
        item = stack.pop()
        print('LinkedListStack pop: {}'.format(item))


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
