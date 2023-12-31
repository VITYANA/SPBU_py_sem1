from collections import namedtuple
from dataclasses import dataclass


StackElement = namedtuple("StackElement", ["value", "next"])


@dataclass
class Stack:
    size: int = 0
    head: StackElement = None


def empty(stack: Stack) -> bool:
    return stack.size == 0


def top(stack: Stack):
    if not empty(stack):
        return stack.head.value


def pop(stack: Stack) -> None:
    if not empty(stack):
        stack.head = stack.head.next
        stack.size -= 1


def push(stack: Stack, value: any) -> None:
    new_element = StackElement(value, stack.head)
    stack.head = new_element
    stack.size += 1


def size(stack):
    return stack.size


def create_stack():
    new_stack = Stack()
    return new_stack


if __name__ == "__main__":
    stack1 = create_stack()
    for i in range(3):
        push(stack1, i)
    print(size(stack1))
    print(top(stack1))
    print(empty(stack1))
    for i in range(3):
        pop(stack1)
    print(size(stack1))
    print(top(stack1))
    print(empty(stack1))
