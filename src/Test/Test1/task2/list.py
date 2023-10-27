from dataclasses import dataclass


@dataclass
class Node:
    value: any = None
    next: any = None
    previous: any = None


@dataclass
class List:
    size: int = 0
    head: Node = None
    tail: Node = None


def create():
    return List()


def head(list):
    return list.head.value


def insert(list, value, index):
    if index <= 0:
        index_len = abs(index)
    else:
        index_len = index + 1
    if index_len > list.size + 1:
        raise ValueError("List index out of range.")
    if list.size == index == 0:
        list.head = Node(value, None, None)
    else:
        if index > 0:
            list_copy = list.head
            for i in range(index_len):
                list_copy = list_copy.next
            tail = list_copy.next
            list_copy.next = Node(value, tail, list_copy.previous)
        else:
            list_copy = list.tail
            for i in range(index_len):
                list_copy = list_copy.previous
            head = list_copy.previous
            list_copy.previous = Node(value, head, list_copy.next)
    list.size += 1


def tail(list):
    return list.tail.value


def locate(list, value):
    list_copy = list.head
    for i in range(list.size):
        if list_copy.value == value:
            return i
        list_copy = list_copy.next
    raise ValueError("No such element in list.")


def retrieve(list, index):
    if index < 0:
        index_len = abs(index) - 1
    else:
        index_len = index
    if index_len > list.size - 1:
        raise ValueError("List index out of range.")
    if index >= 0:
        list_copy = list.head
        for i in range(index):
            list_copy = list_copy.next
    else:
        list_copy = list.tail
        for i in range(index_len):
            list_copy = list_copy.previous
    return list_copy.value


def delete(list, index):
    if index < 0:
        index_len = abs(index) - 1
    else:
        index_len = index
    if index_len > list.size - 1:
        raise ValueError("List index out of range.")
    if index == 0:
        list.head = list.head.next
    elif index > 0:
        list_copy = list.head
        for i in range(index - 1):
            list_copy = list_copy.next
        tail = list_copy.next
        tail = tail.next
        list_copy.next = tail
    else:
        list_copy = list.tail
        for i in range(index_len):
            list_copy = list_copy.previous
        head = list_copy.previous
        head = head.next
        list_copy.previous = head
    list.size -= 1
