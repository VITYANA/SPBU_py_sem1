from dataclasses import dataclass
from typing import Optional, TypeVar, Generic

Value = TypeVar("Value")


@dataclass
class Node(Generic[Value]):
    value: Value
    next: Optional["Node[Value]"] = None


@dataclass
class Queue(Generic[Value]):
    size: int = 0
    head: Optional["Node[Value]"] = None
    tail: Optional["Node[Value]"] = None


def create_queue():
    return Queue()


def is_empty(queue):
    return queue.size == 0


def get_size(queue):
    return queue.size


def enqueue(queue, element):
    if is_empty(queue):
        queue.head = Node(element, None)
        queue.tail = queue.head
    else:
        queue.tail.next = Node(element, None)
        queue.tail = queue.tail.next
    queue.size += 1


def dequeue(queue):
    if is_empty(queue):
        raise AttributeError("Queue is empty.")
    if queue.size > 1:
        return_element = queue.head.value
        queue.size -= 1
        queue.head = queue.head.next
        return return_element


def head(queue):
    if queue.size == 0:
        raise AttributeError("Queue is empty.")
    return queue.head.value
