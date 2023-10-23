from dataclasses import dataclass


@dataclass
class Node:
    value: any
    next: any


@dataclass
class Queue:
    size: int = 0
    head: Node = None
    tail: Node = None


def create_queue():
    return Queue()


def is_empty(queue):
    return queue.size == 0


def size(queue):
    return queue.size


def enqueue(queue, element):
    if is_empty(queue):
        queue.head = Node(element, None)
        queue.tail = queue.head
    else:
        new_element = Node(element, None)
        queue.tail.next = new_element
        queue.tail = queue.tail.next
    queue.size += 1


def dequeue(queue):
    if is_empty(queue):
        raise AttributeError("Queue is empty.")
    elif queue.size > 1:
        return_element = queue.head.value
        queue.size -= 1
        queue.head = queue.head.next
        return return_element
    else:
        queue.size -= 1
        return queue.head.value


def head(queue):
    if queue.size == 0:
        raise AttributeError("Queue is empty.")
    else:
        return queue.head.value
