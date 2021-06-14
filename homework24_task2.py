from typing import Any

class Stack:
    def __init__(self, size=10):
        self.__stack = []
        self.__size = size

    @property
    def empty(self) -> bool:
        return not bool(self.__stack)

    def peek(self) -> Any:
        if not self.empty:
            return self.__stack[-1]

    def pop(self) -> Any:
        if not self.empty:
            return self.__stack.pop()
        raise IndexError

    def push(self, data: Any) -> bool:
        if len(self.__stack) == self.__size:
            return False
        self.__stack.append(data)
        return True

    def __len__(self):
        return len(self.__stack)

    def search_and_extract(self, data: Any):
        stack2 = self.__class__(self.__size)
        while not self.empty:
            x = self.pop()
            if x == data:
                break
            else:
                stack2.push(x)
        while not stack2.empty:
            y = stack2.pop()
            self.push(y)
        return x == data

    def __repr__(self):
        return str(self.__stack)


def balance(expr):
    stack1 = Stack()
    open_brek = '{[('
    close_brek = '}])'
    para = dict(zip(close_brek, open_brek))
    for i in expr:
        if i in open_brek:
            stack1.push(i)
        elif i in close_brek:
            if not stack1.empty and para[i] == stack1.peek():
                stack1.pop()
            else:
                return False
    return stack1.empty

if __name__ == '__main__':
    que = Stack()
    for i in "qwerty":
        que.push(i)
    print(que)
    print(que.search_and_extract('t'))
    print(que)
    print(balance('{}fdgjdfgkg{}([{}])[]]'))
    exit(0)

