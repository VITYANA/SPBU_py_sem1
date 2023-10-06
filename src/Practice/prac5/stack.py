from collections import namedtuple
from dataclasses import dataclass


StackElement = namedtuple("StackElement", ["value", "next"])


@dataclass
class Stack:
    size: int
    head: StackElement = None


def empty(stack: Stack) -> bool:
    return stack.size == 0


def top(stack: Stack):
    if stack.size != 0:
        return stack.head.value


def pop(stack: Stack) -> None:
    stack.head = stack.head.next
    stack.size -= 1


def push(stack: Stack, value: any) -> None:
    new_element = StackElement(value, stack.head)
    stack.head = new_element
    stack.size += 1


def size(stack):
    return stack.size


if __name__ == "__main__":
    stack1 = Stack(0)
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
